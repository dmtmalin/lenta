# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import architect
from django.core.cache import cache

from django.db import models


class RubricQuerySet(models.QuerySet):
    def cache_get_or_create(self, key, defaults=None, **kwargs):

        try:
            cache_key = kwargs[key]
        except KeyError:
            raise AttributeError(u'Cache key not contained in transmitted model params')

        rubric, created = cache.get(cache_key), False
        if not rubric:
            rubric, created = super(RubricQuerySet, self).get_or_create(defaults, **kwargs)
            cache.set(cache_key, rubric)

        return rubric, created


class Rubric(models.Model):
    title = models.CharField(u'Название', max_length=255)

    objects = RubricQuerySet.as_manager()

    class Meta:
        verbose_name = u'Рубрика'
        verbose_name_plural = u'Рубрики'

    def __unicode__(self):
        return self.title


@architect.install('partition', type='range', subtype='date', constraint='month', column='published')
class News(models.Model):
    title = models.CharField(u'Название', max_length=255)
    description = models.TextField(u'Описание')
    published = models.DateTimeField(u'Дата публикации')
    link = models.URLField(u'Ссылка')
    rubric = models.ForeignKey(Rubric, verbose_name=u'Рубрика')

    class Meta:
        ordering = ('-published',)
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def __unicode__(self):
        return self.title
