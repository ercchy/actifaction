from unittest import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class TestViews(TestCase):
    client = Client()

    def test_urls(self):
        index_response = self.client.get(reverse('web.index'))
        self.assertEquals(200, index_response.status_code)
        self.assertEquals('value', index_response.context[-1]['test'])

