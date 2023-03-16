import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('voice', 'ru')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speaker(text):
    engine.say(text)
    engine.runAndWait()