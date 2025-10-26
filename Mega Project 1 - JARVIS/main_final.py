import speech_recognition as sr     # as : intead of using speech_recognition we may use sr instead in the later part of program 
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognize = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c255f98a87954246b63f1a6e9a97b9ca"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])



if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen to the wake word 'Jarvis'

        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=2 ,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")

                #Listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source , timeout=2 ,phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error:", e)