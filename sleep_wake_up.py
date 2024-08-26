import pyttsx3
import datetime
import time

def say(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        say("Good Morning Sir!")
    elif 12 <= hour < 18:
        say("Good Afternoon Sir!")
    else:
        say("Good Evening Sir!")

def go_to_sleep():
    say("Ok sir, I am going to sleep. You can wake me up anytime by saying 'wake up'.")
    time.sleep(3)  # Simulate the assistant going to sleep

def wake_up():
    wish_me()  # Greet according to the time