import os
import speech_recognition as sr


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


while True:

    Wake_up=takeCommand()
    if 'wake up' in Wake_up:
        print("Starting your program Jarvis")
        os.startfile('D:\\Voice Assistant\\VoiceAssistant.py')
    else:
        print("Working in Background......")