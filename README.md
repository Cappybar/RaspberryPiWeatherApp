Simple weather app for small raspberry pi display, based on pygame and OpenWeather.

![demo](https://github.com/user-attachments/assets/0c178bb6-be7c-44bb-bf36-910018cb88d5)

Requirements:<br>
-Raspberry Pi<br>
-LCD gpio display<br>
-Python3.10<br>
-OpenWeatherApi key

Instruction
1. To make this work, you will have to first make an account on OpenWeather website: https://openweathermap.org/ 
2. Then git clone this repository and cd into it
3. Copy your api key from: https://home.openweathermap.org/api_keys, and replace it in Config.json <br>(You will have to wait up to 2h for your api key to activate)
4. While you're in Config.json, replace your city name to the one you'd like
5. Run pip3 install -r requirements.txt
6. Run python3 main.py
