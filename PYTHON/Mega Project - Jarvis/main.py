
import musicLibrary
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import webbrowser 
import pyttsx3

recognizer = sr.Recognizer()
# engine = pyttsx3.init()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('volume',1.0)
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen(duration=3 , fs=16000):
    '''
    Record audio using sounddevice and convert it into a format speech_recognition understand

    '''
    print("Listening....")
    recording = sd.rec(int(duration*fs), samplerate=fs , channels=1 , dtype="int16")
    sd.wait()
    audio_data = sr.AudioData(recording.tobytes(), fs,2)
    return audio_data

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)



if __name__ == "__main__":
    speak("Intializing Jarvis....")
    # listen for the wake word "Jarvis"
    # obtain the audio from microphone 
    audio = listen()

   
    print("Recognitizing...")
    while True:
        try:
            word = recognizer.recognize_google(audio)
            print("You said: ", word)
            # print("Debug lower:", repr(word.lower()))
            if "hello" in word.lower() :
                speak("Ji Bolo")
                print("Jarvis Active...")
                audio = listen()
                command = recognizer.recognize_google(audio)
                processCommand(command)
            audio = listen()
            
   
        except sr.UnknownValueError:
            print ("Sorry Samaj nhi aaya.")
            audio = listen()
            
        except sr.RequestError as e:
            print("Google API Error {0}".format(e))
            audio = listen()
            
            

 