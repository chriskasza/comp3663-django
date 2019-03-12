from django.test import TestCase

class testWeather(TestCase):
    def setUp(self):
       print('hello')

    def test_weather(self):
         self.assertEqual('efewfwf', 'efewfwf')