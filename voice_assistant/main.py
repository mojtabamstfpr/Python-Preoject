import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
    engine.say("You said " + command)
    engine.runAndWait()
except:
    print("Could not understand.")