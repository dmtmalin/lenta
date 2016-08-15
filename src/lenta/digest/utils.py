# -*- coding: utf-8 -*-
import os
from datetime import datetime
from time import mktime

import trml2pdf
from django.template.loader import get_template
from django.templatetags.static import static
from django.utils.timezone import make_aware
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from lenta.digest.models import News
from django.conf import settings


def struct_time_to_datetime(time):
    return datetime.fromtimestamp(mktime(time))


def struct_time_to_datetime_tz(time):
    return make_aware(struct_time_to_datetime(time))


def last_news(entries):
    last_published = News.objects.values_list('published', flat=True).first()
    return filter(
        lambda e: struct_time_to_datetime_tz(e.published_parsed) > last_published, entries)\
        if last_published else entries


class Report(object):
    __instance = None

    def __new__(cls):
        if Report.__instance is None:
            Report.__instance = object.__new__(cls)
            font = ''.join((settings.BASE_DIR, static('lenta/fonts/DejaVuSans.ttf'),))
            bold_font = ''.join((settings.BASE_DIR, static('lenta/fonts/DejaVuSans-Bold.ttf'),))
            pdfmetrics.registerFont(TTFont('DejaVuSans', font, 'utf-8'))
            pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', bold_font, 'utf-8'))
        return Report.__instance

    def generate(self, news):
        template = get_template('digest/report.rml')
        html = template.render({'news': news})
        return trml2pdf.parseString(html.encode('utf-8'))
