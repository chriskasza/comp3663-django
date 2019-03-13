from django.test import TestCase
from djangoapp import weather


class testWeather(TestCase):
    def setUp(self):
      print('Testing weather')
      mock = {
          "main": {"temp": 274.15},  # We are testing the kelvin conversion we get back from the api.
          "wind": {"speed": 33},
          "clouds": {"all": 22},
      }
      self.firstMock = weather.Weather(mock)
   
    def test_jsonMapping(self):
       self.assertEqual(self.firstMock.kelvin, 274.15)
       self.assertEqual(self.firstMock.wind, 33)
       self.assertEqual(self.firstMock.clouds, 22)

    def test_celcius(self):
      self.assertEqual(self.firstMock.celcius(), 1)

    def test_slogan(self):
       self.assertEqual(self.firstMock.generateSlogan(), "It's a windy day!")
   
    def test_slogan2(self):
       self.firstMock.wind = 0
       self.assertEqual(self.firstMock.generateSlogan(), "It's a nice day")
   