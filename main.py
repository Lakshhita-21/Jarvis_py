import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

if__name__ = "__main__"
speak("Intilizing jarvis")

while True:
    # listen to the wake word jarvis 
    #obtain the audio from microphone
    r = sr.Recognizer()
    print("recognizing....")
    try:
        with sr.Microphone() as source:
            print("listning...")
            audio = r.listen(source , timeout=5, phrase_time_limit=5)
        command = r.recognize_google(audio)
        print(command)
        # if (command.lower()== "jarvis"):
        #     speak("ya")
    except Exception as e:  
        print("Error:", type(e).__name__, e)
