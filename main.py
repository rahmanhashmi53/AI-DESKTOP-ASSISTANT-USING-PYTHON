import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import openai
from config import apikey
import random
import requests
import pywhatkit
import wikipedia
import pyautogui
import cv2
from music_control import MusicController
from sleep_wake_up import wish_me, go_to_sleep, wake_up
from Dictapp import openappweb, closeappweb
from NewsRead import latestnews
from speedtest import Speedtest
from plyer import notification  # Importing plyer for notifications
from bs4 import BeautifulSoup  # Importing BeautifulSoup for web scraping

music_controller = MusicController()

def play_music():
    music_controller.play_random_music()

def pause_music():
    music_controller.pause_music()

def resume_music():
    music_controller.resume_music()

def stop_music():
    music_controller.stop_music()

def next_song():
    music_controller.next_song()
def alarm(query):
    with open("Alarmtext.txt", "w") as timehere:
        timehere.write(query.strip())
    os.startfile("alarm.py")

def remember(query):
    rememberMessage = query.replace("remember that", "").replace("jarvis", "").strip()
    say("You told me to remember that " + rememberMessage)
    with open("Remember.txt", "a") as remember:
        remember.write(rememberMessage + "\n")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    say("Screenshot taken and saved as screenshot.png")

def take_selfie():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        say("Unable to access the camera")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("selfie.png", frame)
        say("Selfie taken and saved as selfie.png")
    else:
        say("Failed to take a selfie")
    cap.release()
    cv2.destroyAllWindows()

def recall():
    try:
        with open("Remember.txt", "r") as remember:
            remembered = remember.read().strip()
            if remembered:
                say("You told me to remember that " + remembered)
            else:
                say("You haven't told me to remember anything yet.")
    except FileNotFoundError:
        say("You haven't told me to remember anything yet.")


def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    say("Let's play Rock, Paper, Scissors! We will play 3 rounds.")

    for _ in range(3):
        computer_choice = random.choice(choices)
        say("Choose rock, paper, or scissors")

        user_choice = takeCommand().lower()
        say(f"You chose {user_choice}. I chose {computer_choice}.")

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win this round!"
            user_score += 1
        else:
            result = "I win this round!"
            computer_score += 1

        say(result)
        print(result)

    if user_score > computer_score:
        final_result = "You are the overall winner!"
    elif computer_score > user_score:
        final_result = "I am the overall winner!"
    else:
        final_result = "It's a tie overall!"

    say(f"The final score is - You: {user_score}, Me: {computer_score}.  {final_result}")
    print(f"The final score is - You: {user_score}, Me: {computer_score}.  {final_result}")


def GPT(query, prompt):
    # Define the logic for generating prompts here
    pass  # Placeholder, replace with actual code

def get_weather(api_key, city):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        weather_description = data['current']['condition']['text']
        temperature_celsius = data['current']['temp_c']
        return (f"Weather in {location},{country} is : {weather_description}, and Temperature is : {temperature_celsius}°C")
    else:
        return (f"Failed to retrieve weather data. Status Code: {response.status_code}")

# Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key
api_key = 'YOUR_API_KEY'
city_name = 'Hyderabad'  # Replace with the desired city name

get_weather(api_key, city_name)

chatStr = ""
def chat(query):
    global chatStr
    try:
        openai.api_key = apikey
        chatStr += f" Sir: {query}\n Jarvis: "

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Jarvis created by Tony Stark"},
                {"role": "user", "content": chatStr},
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        say(response['choices'][0]['message']['content'])
        chatStr += f"{response['choices'][0]['message']['content']}\n"
        return response['choices'][0]['message']['content']
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return "Sorry, I could not understand what you said."

def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for prompt: {prompt} \n ****************** \n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named Jarvis created by Tony Stark."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    generated_text = response['choices'][0]['message']['content']
    text += generated_text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}", "w") as f:
        f.write(text)

    say(f"Open AI response saved to file.")


def generate_image(prompt):
    try:
        openai.api_key = apikey
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="512x512"  # Size of the generated image
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        say(f"Error generating image: {e}")
        print(f"Error generating image: {e}")
        return None

def say(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    # Setting voice property to the first voice in the list
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing ...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return "Sorry, I could not understand what you said."
        except sr.RequestError as e:
            print(f"Some Error occurred.Sorry from Jarvis: {e} ")
            return "Some Error occurred.Sorry from Jarvis"



if __name__ == '__main__':
    wish_me()
    say('JARVIS AI', rate=130)

    while True:
        print("Listening ...")
        query = takeCommand().lower()

        if "go to sleep" in query:
            go_to_sleep()
            while True:
                query = takeCommand()
                if "wake up" in query:
                    wake_up()
                    break
            continue

        found_command=False


        if not found_command:
            # Check other commands and trigger OpenAI chat if no specific command is found
            if "play music" in query or "set the mood" in query:
                play_music()
                found_command = True

            elif "pause music" in query:
                pause_music()
                found_command = True

            elif "resume music" in query:
                resume_music()
                found_command = True

            elif "stop music" in query:
                stop_music()
                found_command = True

            elif "next song" in query:
                next_song()
                found_command = True

            elif "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")
                found_command = True

            elif "Using artificial Intelligence".lower() in query.lower():
                ai(query)
                found_command = True

            elif "hello".lower() in query.lower():
                say("Hello sir, how are you ?")
                found_command = True

            elif "i am fine".lower() in query.lower():
                say("that's great, sir")
                found_command = True

            elif "how are you".lower() in query.lower():
                say("Perfect, sir")
                found_command = True

            elif "thank you".lower() in query.lower():
                say("you are welcome, sir")
                found_command = True

            elif "well done" in query.lower() or "very good" in query.lower():
                say("Thank you, sir")
                found_command = True

            elif "exit".lower() in query.lower():
                say("Goodbye, sir!")
                exit()
                found_command = True

            elif "reset chat".lower() in query.lower():
                chatStr = ""
                say("Chat reset sir ...")
                found_command = True

            elif "weather".lower() in query.lower():
                api_key = 'ea70e10718e04ed698d130749240102'
                city_name = 'Hyderabad'  # Replace with the desired city name
                weather_info = get_weather(api_key, city_name)
                print(weather_info)
                say(weather_info, rate=150)
                found_command = True

            elif "set an alarm" in query:
                print("input time example:- 12:57:08")
                say("Set the time")
                a = input("Please tell the time (HH:MM:SS): ")
                alarm(a)
                say("Done, sir")
                found_command = True

            elif "open" in query:
                openappweb(query)
                found_command = True

            elif "close" in query:
                closeappweb(query)
                found_command = True

            elif "remember that" in query:
                rememberMessage = query.replace("remember that", "").strip()
                rememberMessage = rememberMessage.replace("jarvis", "").strip()
                say("You told me to remember that " + rememberMessage)
                with open("Remember.txt", "w") as remember:
                    remember.write(rememberMessage)

            elif "what do you remember" in query:
                with open("Remember.txt", "r") as remember:
                    rememberMessage = remember.read().strip()
                if rememberMessage:
                    say("You told me to remember that " + rememberMessage)
                else:
                    say("Sorry, I don't remember anything.")

            elif "news" in query:
                latestnews()
                found_command = True


            elif "internet speed" in query:
                wifi = Speedtest()
                upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                download_net = wifi.download() / 1048576
                print("Wifi download speed is ", download_net)
                print("Wifi Upload Speed is", upload_net)
                say(f"Wifi download speed is {download_net:.2f} Mbps")
                say(f"Wifi upload speed is {upload_net:.2f} Mbps")
                found_command = True

            elif "screenshot" in query:
                take_screenshot()
                found_command = True

            elif "selfie" in query:
                take_selfie()
                found_command = True

            elif "play a game" in query or "rock paper scissors" in query:
                play_game()
                found_command = True

            elif "generate an image" in query:
                say("What would you like me to create?")
                image_prompt = takeCommand().lower()
                image_url = generate_image(image_prompt)
                if image_url:
                    say("Here is the image I created.")
                    webbrowser.open(image_url)
                    print(f"Generated image URL: {image_url}")
                found_command = True

            # elif "ipl score" in query:
            #     url = "https://www.cricbuzz.com/"
            #     page = requests.get(url)
            #     soup = BeautifulSoup(page.text, "html.parser")

            #     try:
            #         team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
            #         team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
            #         team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
            #         team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

            #         print(f"{team1} : {team1_score}")
            #         print(f"{team2} : {team2_score}")

            #         notification.notify(
            #             title="IPL SCORE :- ",
            #             message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
            #             timeout=15
            #         )
            #     except IndexError as e:
            #         print("Error: ", e)
            #         say("Sorry, I couldn't fetch the IPL scores. Please try again later.")
            #     found_command = True

        if not found_command:
            if "google".lower() in query.lower():
                query = query.replace("search google ", "")
                query = query.replace("google", "")
                query = query.replace("jarvis", "")
                query = query.strip()
                try:
                    pywhatkit.search(query)
                    result = wikipedia.summary(query, 1)
                    say(result)
                except:
                    say("No speakable output available")

                found_command = True

            elif "youtube".lower() in query.lower():
                query = query.replace("youtube", "")
                query = query.replace("search youtube ", "")
                query = query.replace("jarvis youtube", "")
                query = query.strip()
                # webbrowser ="https://www.youtube.com/results?search_query=" + query
                try:
                    pywhatkit.playonyt(query)
                    say("Done, Sir")
                except:
                    say("Error occurred while searching YouTube")

                found_command = True

            elif "wikipedia".lower() in query.lower():
                query = query.replace("wikipedia", "")
                query = query.replace("search wikipedia ", "")
                query = query.replace("jarvis", "")
                query = query.strip()
                try:
                    results = wikipedia.summary(query, sentences=2)
                    say(f"According to Wikipedia, {results}")
                except:
                    say("Error occurred while searching Wikipedia")

                found_command = True

            # say(query)
        # Call OpenAI chat only if no specific command is found
        # if not found_command:
        #     print("Chatting..")
        #     chat(query)
