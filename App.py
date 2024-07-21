import pygame as pg
import OpenWeather
import WeatherIcon
import time as t
import json
class App:
    def __init__(self):
        config = json.load(open("Config.json","r",encoding="utf-8"))
        self.api_key = config["api_key"]
        self.city_name = config["city_name"]
        self.SCREEN_HEIGHT = config["screen_height"]
        self.SCREEN_WIDTH = config["screen_width"]
        self.BG_COLORS = (0x51, 0x8d, 0xe7)
        self.running = True

    def run(self):
        pg.init()
        fullscreen = pg.FULLSCREEN
        pg.mouse.set_visible(False)
        screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), flags=fullscreen)
        clock = pg.time.Clock()

        FONT = pg.font.SysFont("Arial", self.SCREEN_HEIGHT // 10)

        open_weather = OpenWeather.Weather(self.api_key, self.city_name)
        weather_json = open_weather.makeCall()
        weather_icon = WeatherIcon.WeatherIcon()
        weather_icon.weatherIcon(weather_json)
        weather_icon.animate()
        response_time = t.time()

        while self.running:
            clock.tick(1)
            screen.fill(self.BG_COLORS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            current_time = t.time()
            if current_time - response_time >= 60:
                response_time = current_time
                weather_json = open_weather.makeCall()
                weather_icon = WeatherIcon.WeatherIcon()
                weather_icon.weatherIcon(weather_json)
                print(f"Making a weather call: {weather_json}")

            city = FONT.render(f"City: {weather_json['name']}", False, (180, 173, 145))
            temperature = FONT.render(
                f"Temperature: {OpenWeather.Weather.ConvertKtoC(weather_json['main']['temp'])}°C", False,
                (180, 173, 145))
            humidity = FONT.render(f"Humidity: {weather_json['main']['humidity']}%", False, (180, 173, 145))
            pressure = FONT.render(f"Air pressure: {weather_json['main']['pressure']} hPa", False, (180, 173, 145))
            weather_icon.animate()

            screen.blit(city, (self.SCREEN_HEIGHT / 4, self.SCREEN_WIDTH / 2.5))
            screen.blit(temperature, (self.SCREEN_HEIGHT / 4, self.SCREEN_WIDTH  / 2.1))
            screen.blit(humidity, (self.SCREEN_HEIGHT / 4, self.SCREEN_WIDTH  / 1.8))
            screen.blit(pressure, (self.SCREEN_HEIGHT / 4, self.SCREEN_WIDTH  / 1.6))
            screen.blit(weather_icon.pygame_icon, (self.SCREEN_HEIGHT // 3, self.SCREEN_WIDTH //40))

            pg.display.flip()

