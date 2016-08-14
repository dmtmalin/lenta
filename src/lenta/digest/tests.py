from datetime import datetime, timedelta

from django.core.cache import cache
from django.test import TestCase
from mixer.backend.django import mixer

from lenta.digest.models import Rubric
from lenta.digest.forms import SendDigestForm


class RubricQuerySetTestCase(TestCase):

    def test_success_cache_get_or_create(self):
        rubric, created = Rubric.objects.cache_get_or_create(key='title', title='test')
        rubric_from_cache = cache.get('test')

        self.assertTrue(created)
        self.assertIsInstance(rubric_from_cache, Rubric)

        rubric, created = Rubric.objects.cache_get_or_create(key='title', title='test')
        rubric_from_cache = cache.get('test')

        self.assertFalse(created)
        self.assertIsInstance(rubric_from_cache, Rubric)

    def test_empty_cache_get_or_create(self):
        mixer.blend(Rubric, title='test_next')
        rubric_from_cache = cache.get('test_next')

        self.assertIsNone(rubric_from_cache)

        self.assertRaises(AttributeError, Rubric.objects.cache_get_or_create, key='bad_key', title='test')


class SendDigestFormTestCase(TestCase):

    def test_success_validation(self):
        rubric = mixer.blend(Rubric)
        data = {
            'begin': datetime.now(),
            'final': datetime.now() + timedelta(seconds=1),
            'rubric': rubric.id,
            'email': 'test@test.com'
        }
        form = SendDigestForm(data=data)
        self.assertTrue(form.is_valid())

    def test_validation_broken_rubric(self):
        data = {
            'begin': datetime.now(),
            'final': datetime.now() + timedelta(seconds=1),
            'rubric': '1',
            'email': 'test@test.com'
        }
        form = SendDigestForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('rubric', form.errors)

    def test_validation_broken_date(self):
        rubric = mixer.blend(Rubric)
        data = {
            'begin': datetime.now() + timedelta(seconds=1),
            'final': datetime.now(),
            'rubric': rubric.id,
            'email': 'test@test.com'
        }
        form = SendDigestForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('begin', form.errors)

    def test_validation_broken_email(self):
        rubric = mixer.blend(Rubric)
        data = {
            'begin': datetime.now(),
            'final': datetime.now() + timedelta(seconds=1),
            'rubric': rubric.id,
            'email': 'broken_email'
        }
        form = SendDigestForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
