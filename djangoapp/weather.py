import json

class Weather(object):

    def __init__(self, data):
        self.data = data
        self.kelvin = data['main']['temp']
        self.wind = int(data['wind']['speed'])
        self.clouds = int(data['clouds']['all'])

    def celcius(self): 
        return int(self.kelvin - 273.15)
        
    def jsonResp(self):
        c = self.celcius()
        return json.dumps({ "temp": c , "slogan" : self.generateSlogan() })

    def generateSlogan(self):
        if (self.wind > 20):
            return "It's a windy day!"
        elif (self.clouds > 70):
            return "It's cloudy!"
        return "It's a nice day"
