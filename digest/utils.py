# -*- coding: utf-8 -*-
from time import mktime
from datetime import datetime

from django.utils.timezone import make_aware

from digest.models import News


def struct_time_to_datetime(time):
    return datetime.fromtimestamp(mktime(time))


def struct_time_to_datetime_tz(time):
    return make_aware(struct_time_to_datetime(time))


def last_news(entries):
    last_published = News.objects.values_list('published', flat=True).first()
    return filter(
        lambda e: struct_time_to_datetime_tz(e.published_parsed) > last_published, entries)\
        if last_published else entries
