from django.test import TestCase
from django.urls import reverse


class SimpleTest(TestCase):
    def test_index_status(self):
        response = self.client.get(reverse('momentsapp:index'))
        self.assertIn(response.status_code, (200, 302))
