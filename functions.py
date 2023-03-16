import os, webbrowser, sys, requests
import subprocess
import voice
import requests
from bs4 import BeautifulSoup as b

url = 'https://www.anekdot.ru/last/good'

def browser():
    webbrowser.open('https://ya.ru/', new=2)


def yout():
    webbrowser.open('https://www.youtube.com/', new=2)


def radio():
    webbrowser.open('http://the-radio.ru/radio/antenne-bayern-chillout-r421', new=2)


def joke():
    try:
        def parser(url):
            r = requests.get(url)
            soup = b(r.text, 'html.parser')
            anekdots = soup.find_all('div', class_='text')
            return [c.text for c in anekdots]
        list_jokes = parser(url)
        voice.speaker(list_jokes[0])
        del list_jokes[0]
    except:
        voice.speaker('Нет настроения...')


def offpc():
    os.system('shutdown')


def weather():
    try:
        params = {'q': 'Obinitsa', 'units': 'metric', 'lang': 'ru', 'appid': '1912624fd49c501f2986b6ff90fd4a0b'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
    except:
        voice.speaker('Не получилось узнать погоду, сиди дома...')


def offBot():
    sys.exit()


def passive():
    pass