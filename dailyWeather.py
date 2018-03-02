import requests
import pyttsx3

url = 'http://api.openweathermap.org/data/2.5/weather?q=Lubbock&units=imperial&appid=[appid here]'

#openweathermap.org api
json_data = requests.get(url).json()
description = json_data['weather'][0]['description']
temp = json_data['main']['temp']
temp_max = json_data['main']['temp_max']
sentence = "Good morning! The forecast today will be {}. The temperature is currently {} degrees Fahrenheit, with a high of {} degrees today".format(description, int(temp), int(temp_max))
print(sentence)

#sets voice
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)
tts.say(sentence)
tts.runAndWait()
