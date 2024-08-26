# AI DESKTOP ASSISTANT USING PYTHON

Welcome to the AI Desktop Assistant project! This repository contains a Python-based AI assistant designed to perform a variety of tasks, from managing music and taking screenshots to interacting with OpenAI's GPT-3 and providing real-time updates on weather and news. <br>
This assistant, codenamed "Jarvis," is a versatile tool for both productivity and entertainment.

<strong>Features</strong>

Voice Commands: Control the assistant using voice commands for hands-free interaction.<br>
Music Management: Play, pause, resume, and stop music. Change tracks and set the mood.<br>
Screenshots & Selfies: Capture screenshots and selfies with your webcam.<br>
Chat with AI: Interact with OpenAI's GPT-3 for advanced AI-driven conversations.<br>
Weather Updates: Get real-time weather information for any city.<br>
News Updates: Receive the latest news headlines.<br>
Games: Play Rock, Paper, Scissors against the AI.<br>
Image Generation: Generate images based on text prompts using OpenAI's image models.<br>
Custom Commands: Create and recall custom reminders.<br>

<strong>Installation</strong>

<b>Prerequisites</b>

Python 3.x
pip for installing Python packages


<strong>Create a Virtual Environment (Recommended)</strong>

Copy code :
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

<b>Install Dependencies</b>

Make sure you have requirements.txt file in the repository with the following content:

Then run:

pip install -r requirements.txt

<b>Configuration</b>

OpenAI API Key: To use the GPT-3 features, you need an OpenAI API key. <br>
In the file named config.py in the root directory of the project and add YOUR_OPENAI_API_KEY:

apikey = 'YOUR_OPENAI_API_KEY'

Weather API Key: Obtain a Weather API key from WeatherAPI and add it to the relevant part of the code.

Usage

To start the AI Desktop Assistant, run:

python main.py

<strong>Voice Commands</strong>

<b>Music Management:</b>

"play music"<br>
"pause music"<br>
"resume music"<br>
"stop music"<br>
"next song"<br>

<b>Utility Commands:</b>

"take a screenshot"<br>
"take a selfie"<br>
"set an alarm [time]"<br>
"remember that [message]"<br>
"what do you remember"<br>

<b>AI Interaction:</b>

"hello"<br>
"how are you"<br>
"chat with me"<br>
"generate an image [description]"<br>

<b>Information Queries:</b>

"weather in [city]"<br>
"news"<br>
"internet speed"<br>

<b>Games:</b>

"play a game"<br>
"rock paper scissors"<br>

<b>Custom Modules</b>

music_control.py: Manages music playback.<br>
sleep_wake_up.py: Handles sleep and wake-up commands.<br>
Dictapp.py: Manages opening and closing web apps.<br>
NewsRead.py: Fetches and reads the latest news.v


Contributions are welcome! Please submit issues or pull requests to help improve the assistant. Ensure that your changes are well-documented and tested.


Acknowledgments

OpenAI: For providing the GPT-3 API.<br>
WeatherAPI: For weather data.<br>
PyPI: For the various Python packages used.<br>

<>Feel free to explore and extend the functionality of this AI Desktop Assistant. Happy coding!</b>