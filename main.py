import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)

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
        word = r.recognize_google(audio)
        
        if (word.lower()== "jarvis"):
            speak("ya")
            # listen for command
            with sr.Microphone() as source:
                print ("jarvis active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processcommand(command)


    except Exception as e:  
        print("Error:", type(e).__name__, e)
