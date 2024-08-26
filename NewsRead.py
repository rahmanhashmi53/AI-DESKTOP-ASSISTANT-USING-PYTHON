import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    api_key = 'YOUR_API_KEY'  # Replace with your newsapi.org API key
    api_dict = {
        "business" : "Business_API_KEY",
            "entertainment" : "",
            "health" : "",
            "science" :"",
            "sports" :"",
            "technology" :""
            # in the quotation marks place the API_KEY for the related fields
    }

    content = None
    url = None
    speak("Which field news do you want? Business, Health, Technology, Sports, Entertainment, or Science?")

    # Use takeCommand() to get the field input via voice
    from main import takeCommand # Import the takeCommand function from the main module
    field = takeCommand()

    # Find the corresponding URL for the requested news category

    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            break
    else:
        speak("Field not found")
        return

    # Fetch news data from the API

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    # Iterate through the news articles and read out the titles

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        speak(article)
        news_url = articles["url"]
        speak(f"For more information, visit the link")

        # Listen for user input to continue or stop reading news

        a = takeCommand().lower()
        if "continue" in a:
            pass
        elif "stop" in a:
            break

    speak("That's all")
