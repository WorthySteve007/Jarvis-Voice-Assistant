import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import subprocess
import tkinter
import json
import random
import operator
import datetime
import webbrowser
import socket
import os
import smtplib
import ctypes
import time
import shutil
from urllib.request import urlopen



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''
    This function converts your written text into audio by the computer.
    '''
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I hope you are having a nice day.")
    speak("I am Jarvis. How can I help you??")

def takeCommand():
    '''
    It takes microphone input as user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sendergmailadd@gmail.com','senderemailpassword')
    server.sendmail('sendergmailadd@gmail.com',to,content)
    server.close()


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("User name added")
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    
    print("Welcome Mr.", uname.center(columns))
if __name__ =='__main__':
    clear = lambda: os.system('cls')
    
    username()
    wishme()
    while True:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks.org')
        elif 'open codeforces' in query:
            webbrowser.open('codeforces.com')
        elif 'play music' in query:
            music_dir="D:\\Songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Risav Katara He created me")
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me Jarvis")
            print("My friends call me Jarvis")
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif 'you need a break' in query:
            speak('Sir you can call me anytime')
            speak('Just say wake up Jarvis')
            break
        elif 'ip' in query:
            hostname =socket.gethostname()
            IPAddr= socket.gethostbyname(hostname)
            speak(IPAddr)
            print(IPAddr)
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif 'news' in query:
             
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=e57f1773ec0f484f8471bb4693a3e095")
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
        elif 'email' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to = "receivergmailadd@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry cannot send this email due to some error")
        elif 'quit' in query:
            speak("I hope you are happy with my service.")
            speak("Terminating the program sir.")
            break
