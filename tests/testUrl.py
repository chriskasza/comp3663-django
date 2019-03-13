from django.test import TestCase
from djangoapp import urls


class testUrls(TestCase):
    def setUp(self):
        print('Testing urls')

    def test_routes(self):
        self.assertEqual(len(urls.urlpatterns), 2)

    def test_current_weather(self):
        curr = urls.currentWeather(None)
        self.assertFalse(curr is None)