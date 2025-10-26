import speech_recognition as sr     # as : intead of using speech_recognition we may use sr instead in the later part of program 
import webbrowser
import pyttsx3

recognize = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            print("Listening timeout - speak louder or get closer to mic")
        except Exception as e:
            print("Error:", e)