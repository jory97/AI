from time import strftime
import pyttsx3   #pip install pyttsx3
import datetime
from requests.models import encode_multipart_formdata
import speech_recognition as sr  #pip install speechRecognition
import wikipedia #pip install wikipedia                     
#if came out with AttributeError: module 'wikipedia' has no attribute 'summary' 
#try download file in https://github.com/goldsmith/Wikipedia/tree/master/docs 
#change or replace file in your wikipedia file with the downloaded file(wikipedia-master) 
import smtplib 
import webbrowser as wb
import psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random
import wolframalpha #pip install wolframalpha
import json
import requests
from urllib.request import urlopen

engine = pyttsx3.init()
#engine.say('hello world!')
#engine.runAndWait()
wolframalpha_app_id = 'wolframalpha id will go here '

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")  #for 24hr clock
    speak("The current time is")
    speak(Time)

#def time_():
    #Time = datetime.datetime.now().strftime("%I:%M:%S")  #for 12hr clock
    #speak("The current time is")
    #speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Welcome back JORY!')
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour >=6 and hour <12 :
        speak("Good Morning Sir!")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour<24 : 
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")         
    
    speak("AI at your service. Please tell me how can I help for you today?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    
    except Exception as e :
        print(e)
        print("Say that again please...")
        return None
    return query 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function , you must enable low security in your gmail which you are going to use as sender

    server.login('username@gmail.com')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())   #dowmloaded file for psutil-master in  https://github.com/giampaolo/psutil 
    speak('CPU is at '+ usage)

    battery = psutil.sensors_battery() #cant write in str() if not cant using percent function
    speak('Battery is at')
    speak(battery.percent)  

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:/Desktop/screenshot.png')

if __name__ == "__main__" :
    
    wishme()

    while True : 
        query = TakeCommand().lower()
        
        if 'time' in query : 
            time_()
        elif 'date' in query :
            date_()    
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences = 3) 
            speak('According to Wikipedia')
            print(result)
            speak(result) 
        elif 'send email' in query:
            try:
                speak("What sohuld i say?")
                content = TakeCommand() 
                #provide reciever email address 

                speak("who is the Reciever?")
                reciever = input("Enter Reciever's Email:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak("Unable to send Email.")    
        
        elif 'search in Firefox' in query:
            speak('What should I search?')
            mozilapath = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'    #location for mozilapath is installation on Computer 

            search = TakeCommand().lower()
            wb.get(mozilapath).open_new_tab(search + '.com')  #only open websites with '.com' at end 

        elif 'search in chrome' in query:
            speak('What should I search?')
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'    #location for chrome is installation on Computer 

            search = TakeCommand().lower()
            wb.get(chrome).open_new_tab(search + '.com')  #only open websites with '.com' at end     

        elif 'search youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()   
            speak("Here We go to YOUTUBE")
            wb.open('http://www.youtube.com/results?search_query='+search_Term) 

        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching...') 
            wb.open('http://www.google.com/results?search_query='+search_Term)   
        
        elif 'cpu' in query :  
            cpu()
        
        elif 'joke' in query:
            joke() 

        elif 'go offline' in query:       #design for ends up 
            speak('Going Offline Sir!')    
            quit()

        elif 'wps' in query:        #design for opening application 
            speak('Opening WPS...')
            wps = r'C:\Users\User\AppData\Local\Kingsoft\WPS Office\ksolaunch.exe'
            os.startfile(wps)
        
        elif 'write a note' in query:
            speak("What should I write, Sir?")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Sir should I include Date and Time?")
            ans = TakeCommand()
            if 'yes' or 'sure' in ans:
                strftime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strftime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes ,SIR!')
            else:
                file.write(notes)    

        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query: 
            screenshot()

        elif 'play music' in query:
            songs_dir = 'D:/songs'    
            music = os.listdir(songs_dir)
            speak('What should I play?')
            speak('select a number...')
            ans = TakeCommand().lower()
            while 'nummber' not in ans and ans != 'random' and ans != 'you chosse':
                speak('I could not understand . Please Try again.')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,100)
            
            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak("What should I remember?")
            memory = TakeCommand()
            speak("You asked me to remember that" + memory)
            remember = open('memory.txt','w')
            remember.write(remember) 
            remember.close()   

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak("You asked me to remember that" + remember.read())

        elif 'news' in query: #cant use for news 
            try:
                jsonObj = urlopen("https://news.google.com/topstories")    
                data = json.load(jsonObj)
                i = 1 

                speak('Here are some TOP headlines from the Entertainment Industry')
                print('=======TOP HEADLINES=========='+'\n')
                for item in data['articles']:
                    print(str(i)+'.'+ item['item']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))        
        
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("http://www.google.com/maps/place/"+ location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id) 
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is:' + answer)  
            speak('The Answer is:' + answer)  









