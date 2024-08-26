import pyttsx3
import datetime
import os
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def read_alarm_time(file_path):
    try:
        with open(file_path, "rt") as extractedtime:
            alarm_time = extractedtime.read().strip()
        return alarm_time
    except FileNotFoundError:
        speak("Alarm time file not found.")
        return None

def parse_alarm_time(time_str):
    try:
        alarm_time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
        return alarm_time
    except ValueError:
        speak("Invalid time format in the alarm time file.")
        return None

def ring(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().time()
        if (current_time.hour == alarm_time.hour and
            current_time.minute == alarm_time.minute and
            current_time.second == alarm_time.second):
            speak("Alarm ringing, sir")
            os.startfile("alarm.mp3")  # Make sure this file exists
            break
        time.sleep(1)  # Sleep for a second to avoid busy-waiting

def main():
    alarm_time_str = read_alarm_time("Alarmtext.txt")
    if alarm_time_str:
        alarm_time = parse_alarm_time(alarm_time_str)
        if alarm_time:
            ring(alarm_time)

if __name__ == "__main__":
    main()
