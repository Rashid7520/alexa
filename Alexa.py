import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
#import pyaudio

listenner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()

engine.say('Hello Rashid, I am your virtual assistant. how can i help you?')
engine.runAndWait()

def take_command():
     # (<-- !!!)
    try:
        
        with sr.Microphone() as source:
            print("listening....")
            voice = listenner.listen(source)
            command = listenner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'song' in command:
        song = command.replace('song', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is" + time)

    elif 'who ' in command:
        person = command.replace('who ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'are you single' in command:
        talk('No, i am in a relationship with your wifi') 

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'wikipedia' in command:
        ansu = command.replace('wikipedia', '')
        answer = wikipedia.summary(ansu, sentences=2)
        print(answer)
        talk(answer)
        
    elif 'open youtube' in command:
        print('opening you tube.....')
        talk('opening you tube.')
        webbrowser.open('youtube.com')

    elif 'open whatsapp' in command:
        webbrowser.open('web.whatsapp.com')
        print('opening whatsapp.....')
        talk('opening whatsapp.')

    elif 'open stackoverflow' in command:
        webbrowser.open('stackoverflow.com')
        print('opening Stackoverfolw.....')
        talk('opening Stack overflow .')

    elif 'music' in command:
        music_dir = 'C:\\Music'
        music= os.listdir(music_dir)
        #print(music)
        os.startfile(os.path.join(music_dir, music[5]))

    elif 'open Vs code' in command:
        code_path = "C:\\Users\\Rashid khan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    
    elif 'how are you' in command:
        talk('I am feeling awesome and ready for your command')
    
    elif 'hear me' in command:
        talk('yes, I am getting you Rashid')
    elif 'exit' in command:
        exit()

    else:
        talk('Please say the command again.')
        

while True:
   run_alexa()
