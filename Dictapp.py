import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) # Set the voice to the first available voice
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Dictionary to map application names to their executable commands

dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "camera": "microsoft.windows.camera:",
    "notepad": "notepad"
}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                return
        speak("Application not recognized, sir.")

def closeappweb(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("One tab closed")
    elif "two tabs" in query or "2 tabs" in query:
        for _ in range(2):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Two tabs closed")
    elif "three tabs" in query or "3 tabs" in query:
        for _ in range(3):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Three tabs closed")
    elif "four tabs" in query or "4 tabs" in query:
        for _ in range(4):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Four tabs closed")
    elif "five tabs" in query or "5 tabs" in query:
        for _ in range(5):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Five tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                return
        speak("Application not recognized, sir.")
