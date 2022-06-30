from asyncio import subprocess
from unicodedata import name
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser #for youtube 
import os 
import webbrowser
import smtplib
import pygame
import pygame.camera
import subprocess
from cv2 import *
from cv2 import VideoCapture
from smtplib import SMTP
from cv2 import imshow
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyWindow
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print("The time is",hour,"hours")
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
         speak("Good Afternoon!")
 
    else:
        speak("Good Evening!")

    speak("My name is Jarvis. I am Your AI Assistant sir . Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        r.energy_threshold = 1000
        r.non_speaking_duration = 0.3
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')

        print(f"User said: {query}\n") 
    # used f string
    except Exception as e:
        #print(e)
        print("Say that again please...")   
        return "None"
    return query

def sendEmail(do,content):
    server = smtplib,SMTP('smtp@gmail.com',465)
    server.ehlo() 
    server.starttls()
    server.login('uphaars.cs.20@nitj.ac.in','20030210')
    server.sendmail('uphaars.cs.20@nitj.ac.in',do,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #converting in lower case
        #Logic for accepting tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datatime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")
        
        elif 'play music' in query:
            codePath = "C:\\Users\\HP\\OneDrive\\Desktop\\Who-Says_320(PagalWorld).mp3"
            os.startfile(codePath)
        
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india')


        elif 'who made you' in query or 'who created you' in query or "who discovered you" in query:
            speak("Here are my Creators")
            print("Creators -- Uphaar Sharma, Yogin Pahuja")
        
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        
        elif 'email to me' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "uphaarkamal2003@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry unable to send this moment")

        elif 'search' in query:
            speak("Searching....")
            query=query.replace("search","")
            webbrowser.open_new_tab(query)
        
        elif 'capture photo' in query:
                cam_port = 0
                cam = VideoCapture(cam_port)
                result, image = cam.read()
  
                if result:

                 imshow("Uphaar", image)

                 imwrite("Uphaar.png", image)
  
                 waitKey(0)
                 destroyWindow("Uphaar")

                else:
                 print("No image detected. Please! try again")


        elif 'log out' or 'shutdown' in query:
            speak("Logging off the computer within 10 seconds, make sure to close all the apllications")
            os.system("shutdown /s /t 1")
