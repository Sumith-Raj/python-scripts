# pip install pyttsx3
import pyttsx3

while True:
    engine = pyttsx3.init()
    engine.say(input('type here'))
    engine.runAndWait()
