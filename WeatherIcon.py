import os
import pygame


class WeatherIcon():
    def __init__(self):
        self.weather_type = "unk"
        self.icons_list = []
        self.icons_str = "assets//unk//"
        self.pygame_icon = pygame.image.load(self.icons_str + "unk1.png")
        self.icon_counter = 0

    def loadIcons(self):
        self.icons_list.clear()
        for file in os.listdir(self.icons_str):
            path = os.path.join(self.icons_str, file)
            if os.path.isfile(path):
                self.icons_list.append(path)

    def weatherIcon(self, weather_json):
        try:
            match weather_json["weather"][0]["main"]:
                case "Clear":
                    self.icons_str = "assets//sun//"
                case "Clouds":
                    self.icons_str = "assets//clouds//"
                case "Rain":
                    self.icons_str = "assets//rain//"
                case "Thunderstorm":
                    self.icons_str = "assets//thunder//"
                case "Drizzle":
                    self.icons_str = "assets//rain//"
                case "Mist":
                    self.icons_str = "assets//rain//"
                case "Snow":
                    self.icons_str = "assets//snow//"
                case _:
                    self.icons_str = "assets//unk//"
            self.loadIcons()
            print(weather_json["weather"][0]["main"])
        except Exception as e:
            if "cod" in weather_json.keys():
                print(weather_json["cod"])
                match str(weather_json["cod"]):
                    case "401":
                        raise Exception("Api key not found, fix your config, or wait 2h for your api_key to activate")
                    case "400":
                        raise Exception("City not found, fix your config")
                    case _:
                        print("Something wrong")
            else:
                self.icons_str = "assets//unk//"
                self.loadIcons()

    def animate(self):
        if self.icon_counter > len(self.icons_list) - 1:
            self.icon_counter = 0
        self.pygame_icon = pygame.image.load(self.icons_list[self.icon_counter])
        self.icon_counter += 1
