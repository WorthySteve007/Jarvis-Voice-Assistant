import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib



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

if __name__ =='__main__':
    #speak("Risav Katara is a good Boy")
    wishme()
    while True:
    # if 1:
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
