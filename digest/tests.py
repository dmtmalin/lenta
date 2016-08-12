from django.test import TestCase

from digest.models import Rubric
from django.core.cache import cache

from mixer.backend.django import mixer


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

    def test_failed_cache_get_or_create(self):
        mixer.blend(Rubric, title='test_next')
        rubric_from_cache = cache.get('test_next')

        self.assertIsNone(rubric_from_cache)

        self.assertRaises(AttributeError, Rubric.objects.cache_get_or_create, key='bad_key', title='test')
