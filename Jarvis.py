
import speech_recognition as sr
import webbrowser
import openai
from config import apikey
import datetime
import pyttsx3
import os
from config import apikey
import requests
import requests
import requests
import requests

def search_youtube(query):
    """
    Searches for songs and videos on YouTube using the YouTube Data API.

    Args:
    - query (str): The search query to use.

    Returns:
    - dict: A dictionary containing the API response or None in case of an error.
    """
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",  # Restricting search to videos
        "key": "AIzaSyCWidS7as0E6eJFi9MlYHaebqIRv-OoGTU" , # Replace with your actual YouTube API key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def search():
    say("Presenting the Songs Movies and Videos..!")
    print("Presenting the Songs Movies and Videos..!")
    query = takeCommand()
    print(query)
    if query:
        youtube_data = search_youtube(query)
        for item in youtube_data.get("items", []):
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            print(f"Title: {video_title}")
            print(f"Watch here: https://www.youtube.com/watch?v={video_id}")
            print()
            say(f"Title: {video_title}")
            print("Do you want to watch this video? (go for it/don't want): ")
            say("Do you want to watch this video? (go for it/don't want): ")
            choice = takeCommand()
            print(choice)
            if choice =="go for it" :
                webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
                break
            elif choice == "don't want" in takeCommand().lower():
                print("Okay Raja!")
                say("Okay Raja!")
        else:
            print("Failed to search on YouTube.")
import requests

def news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to retrieve news.')
        return None

def display_news(api_key):
    news_data = news(api_key)

    if news_data and 'articles' in news_data:
        for article in news_data['articles']:
            print(article['title'])
            # You can use the say function here for text-to-speech
            say(article['title'])
            print(article['description'])
            say(article['description'])
    else:
        print('Failed to retrieve news.')

# Replace 'your_api_key_here' with your actual NewsAPI key.
api_key ='efa1aba69e91444b893a98ba64c6ad09'


def get_weather(api_key, city):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # You can add a print statement here to debug
    else:
        print('Error:', response.status_code)
        return None

def main():
    api_key = '371f05d3fcc143ffa9e170125241203'  # Make sure this is correct and active
    city = 'New Delhi'
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(weather_data)  # Debugging: print the entire response to inspect
        current = weather_data['current']
        print(f"Weather in {city}:")
        say(f"Weather in {city}:")
        print(f"Condition: {current['condition']['text']}")
        say(f"Condition: {current['condition']['text']}")
        print(f"Temperature: {current['temp_c']}°C")
        say(f"Temperature: {current['temp_c']}°C")
        print(f"Humidity: {current['humidity']}%")
        say(f"Humidity: {current['humidity']}%")
        print(f"Pressure: {current['pressure_mb']} hPa")
        say(f"Pressure: {current['pressure_mb']} hPa")
    else:
        print("Failed to retrieve weather data.")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Raja: {query}\nJarvis: "
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.makedirs("Openai")

    with open(f"Openai/{''.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            say("Sorry, I did not get that.")
            return "None"
    return query

if __name__ == '__main__':
    print('Welcome to Jarvis A.I',)
    say("I am your Jarvis Sir. Please Tell me Sir How May I help You from my Knowledge!")
    while True:
        query = takeCommand().lower()

        # Define sites to open
        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.com",
            "google": "https://www.google.com",
            "amazon": "https://www.amazon.com",
            "jioCinema": "https://www.jiocinema.com",
            "linkedin": "https://www.linked.com",
            "netflix": "https://www.netflix.com",
            "sonyliv": "https://www.sonyliv.com",
            "chat gpt": "https://www.chatgpt.com",

        }

        for key, url in sites.items():
            if f"open {key}" in query:
                say(f"Opening {key} sir...")
                webbrowser.open(url)
                break

        if "open music" in query:
            # Replace with the path to your music file or application
            musicPath = "C:\\Path\\To\\Your\\Music\\File.mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir, the time is {strTime}")
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                    say("Good Morning Sir, Wish You the Best Day!")
                    print("Good Morning Sir, Wish You the Best Day!")
            elif hour >= 12 and hour < 17:
                    say("Good Afternoon Sir!")
                    print("Good Afternoon Sir!")
            elif hour >= 17 and hour < 20:
                    say("Good Evening Sir!")
                    print("Good Evening Sir!")
            else:
                    say("Good Night Sir, I wish the Good Night")
                    print("Good Night Sir, I wish the Good Night")

        # Add more elif blocks for other commands
        # Remember to replace macOS specific paths and use Windows paths or application names

        elif "Using AI".lower() in query.lower():
            ai(prompt=query)
        elif "What is the weather".lower() in query.lower():
            main()
        elif " news".lower() in query.lower():
            display_news(api_key)
        elif "current date".lower() in query.lower():
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            say(f"Sir, today's date is {current_date}")
        elif "Songs".lower() in query.lower():
            search()
        elif "Movies".lower() in query.lower():
            search()
        elif "Videos".lower() in query.lower():
            search()
        elif "jarvis stop" in query:
            say("Goodbye!")
            break

        elif "reset chat" in query:
            chatStr = ""
        else:
            chat(query)
