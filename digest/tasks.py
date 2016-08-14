# -*- coding: utf-8 -*-
from __future__ import absolute_import

import feedparser

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail.message import EmailMessage
from django.core.serializers import deserialize

from digest.models import Rubric, News
from digest.utils import struct_time_to_datetime_tz, last_news, Report

from lenta.celery import app

logger = get_task_logger(__name__)


@shared_task
def grab(url, versions_support):
    logger.info(u'Start grab task from %s' % (url, ))

    rss = feedparser.parse(url)

    if rss.version in versions_support:
        for item in last_news(rss.entries):
            rubric_title = item.tags[0].term if item.tags > 0 else None

            if not rubric_title:
                return logger.error(u"Can't find rubric in rss")

            r, created = Rubric.objects.cache_get_or_create(key='title', title=rubric_title)

            News.objects.create(title=item.title, description=item.description, rubric=r,
                                published=struct_time_to_datetime_tz(item.published_parsed), link=item.link)

            logger.info(u'Grab news %s' % (item.link, ))
    else:
        logger.warning(u'Rss version not supplied: %s' % (rss.version, ))
    logger.info(u'Grab success finished')


@app.task
def send(serialize_news, email):
    logger.info(u'Start send task')
    news = [item.object for item in deserialize('json', serialize_news)]

    logger.info(u'Generate report')
    pdf = Report().generate(news)

    logger.info(u'Send report to %s', (email, ))
    mail = EmailMessage(subject='Digest news', to=(email, ))
    mail.attach('report.pdf', pdf, 'application/pdf')
    mail.send(fail_silently=False)
    logger.info(u'Send success finished')
