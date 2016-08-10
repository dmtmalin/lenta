# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def grab(url):
    logger.info("Start grab %s" % (url, ))


@shared_task
def send():
    logger.info("Start send")
