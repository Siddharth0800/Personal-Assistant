# *** Made By Siddharth Prakash Singh ***
# On 11 october 2020.....

# ****************************************Personal Assistant****************************************************

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import pyperclip as pc
# import pywhatkit
import time
# import pyaudio
from subprocess import call
import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")
#         speak("Siddharth Sir ,I am your personal assistant .")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")
#         speak("Siddharth Sir ,I am your personal assistant . Please tell me how i can help you")

#     else:
#         speak("Good Evening!")

#         speak("Siddharth Sir ,I am your personal assistant .")

def takeCommand():
    #It takes microphone input from the user and returns string output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"Siddharth Sir said : {query}\n")
        speak("Siddharth Sir said :")
        speak(query)

    except Exception as e:
        print(e)
        print("Say that again please")
        speak("sorry , Siddharth Sir can you say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('siddharthpsingh754@gmail.com', 'siddh.arth_0800')
    server.sendmail(email_name, to, content)
    server.close()

if __name__ == "__main__":
    # wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)




        elif 'youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

        elif 'hai' in query:
            speak("Yes Siddharth Sir")
            call(["python", "C:\\Users\\LENOVO\\Desktop\\Python files\\AI\\ai2.py"])

        elif 'hi' in query:
            speak("Yes Siddharth Sir")
            call(["python", "C:\\Users\\LENOVO\\Desktop\\Python files\\AI\\ai2.py"])

        elif 'jarvis' in query:
            speak("Yes Siddharth Sir")
            call(["python", "C:\\Users\\LENOVO\\Desktop\\Python files\\AI\\ai2.py"])

        elif 'Friday' in query:
            speak("Yes Siddharth Sir")
            call(["python", "C:\\Users\\LENOVO\\Desktop\\Python files\\AI\\ai2.py"])

        elif 'Hriday' in query:
            speak("Yes Siddharth Sir")
            call(["python", "C:\\Users\\LENOVO\\Desktop\\Python files\\AI\\ai2.py"])

        elif 'google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'stackoverflow' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://stackoverflow.com/")

        elif 'search' in query:
            speak("What do you want to search sir")
            print("What do you want to search sir")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://stackoverflow.com")

        elif 'login' in  query:
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin', new=2)


        elif 'exit' in query:
            print("Thank you Siddhart Sir for giving me time")
            speak("Thank you Siddhart Sir for giving me time")
            print("Take care Sir")
            speak("Take care sir")
            exit()



        if 'music' in query:
            music_dir = 'D://SONGS'
            songs = os.listdir (music_dir)
            # speak(songs[0])
            print(songs)
            speak("Which song do you want to listen")
            query = query.replace( "music", "")
            results =  os.startfile(os.path.join(music_dir, songs[0]))
            print(results)


            # print (result)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Siddharth Sir, the time is")
            speak(strTime)
            print (strTime)

        elif 'open code' in query:
            speak("Opening VS code")
            codePath = "C://Users//LENOVO//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Visual Studio Code//Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'Do i have a mail' in query:
            speak("Opening mail")
            mailpath = "C://Users//LENOVO//Desktop//Mail.lnk"
            os.startfile(mailpath)

        elif 'send email' in query:
            try:
                speak("To whom Siddharth Sir")
                email_name = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                # content = "siddh.arth_0800"
                to = "savita17445@gmail.com"
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry  Siddharth Sir. I am not able to send this email")
