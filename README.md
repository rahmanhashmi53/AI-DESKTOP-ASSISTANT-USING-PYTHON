# AI DESKTOP ASSISTANT USING PYTHON

Welcome to the AI Desktop Assistant project! This repository contains a Python-based AI assistant designed to perform a variety of tasks, from managing music and taking screenshots to interacting with OpenAI's GPT-3 and providing real-time updates on weather and news. <br>
This assistant, codenamed "Jarvis," is a versatile tool for both productivity and entertainment.

<H2>Features</H2>

<b>Voice Commands:</b><t> Control the assistant using voice commands for hands-free interaction.<br>
<b>Music Management:</b> <t>Play, pause, resume, and stop music. Change tracks and set the mood.<br>
<b>Screenshots & Selfies:</b><t> Capture screenshots and selfies with your webcam.<br>
<b>Chat with AI:</b> <t>Interact with OpenAI's GPT-3 for advanced AI-driven conversations.<br>
<b>Weather Updates:</b> <t>Get real-time weather information for any city.<br>
<b>News Updates:</b> <t>Receive the latest news headlines.<br>
<b>Games:</b> <t>Play Rock, Paper, Scissors against the AI.<br>
<b>Image Generation:</b> <t>Generate images based on text prompts using OpenAI's image models.<br>
<b>Custom Commands:</b> <t>Create and recall custom reminders.<br>

<H2>Installation</H2>

<b>Prerequisites</b>

Python 3.x
pip for installing Python packages


<H2>Create a Virtual Environment (Recommended)</H2>

<b>Copy code :</b><br>
python -m venv venv <br>
source venv/bin/activate <br> 
<h4> On Windows, use `venv\Scripts\activate`</h4>

<b>Install Dependencies</b>

Make sure you have requirements.txt file in the repository with the following content:

<b>Then run:</b>

pip install -r requirements.txt

<b>Configuration</b>

OpenAI API Key: To use the GPT-3 features, you need an OpenAI API key. <br>
In the file named config.py in the root directory of the project and add YOUR_OPENAI_API_KEY:

apikey = <b>'YOUR_OPENAI_API_KEY'</b>

Weather API Key: Obtain a Weather API key from WeatherAPI and add it to the relevant part of the code.

<b>Usage</b>

To start the AI Desktop Assistant, run:

python main.py

<H2>Voice Commands</H2>

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



<b>Feel free to explore and extend the functionality of this AI Desktop Assistant. Happy coding!</b>
