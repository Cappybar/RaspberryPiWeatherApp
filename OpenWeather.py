import requests

class Weather:
    def __init__(self, api_key, city_name):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.city_name = city_name
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city_name
    def makeCall(self):
        return requests.get(self.complete_url).json()
    @staticmethod
    def ConvertKtoC(temperature):
        return round(temperature-273.15,1)
