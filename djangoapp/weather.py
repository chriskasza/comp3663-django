import json

class Weather(object):

    def __init__(self, data):
        self.data = data
        self.kelvin = data['main']['temp']

    def decode(self): 
        print(self.data['main']['temp'])

    def celcius(self): 
        return int(self.kelvin - 273.15)
    def jsonResp(self):
        c = self.celcius()
        return json.dumps({ "temp": c })
