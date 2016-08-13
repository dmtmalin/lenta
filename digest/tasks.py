# -*- coding: utf-8 -*-
from __future__ import absolute_import

import feedparser

from celery import shared_task
from celery.utils.log import get_task_logger

from digest.models import Rubric, News
from digest.utils import struct_time_to_datetime_tz, last_news

logger = get_task_logger(__name__)


@shared_task
def grab(url, versions_support):
    logger.info(u'Start grab  from %s' % (url, ))

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


@shared_task
def send():
    logger.info("Start send")
