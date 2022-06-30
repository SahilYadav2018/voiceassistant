import datetime
# from email.mime import audio
# from logging import exception
# from unittest import result
# from winreg import QueryReflectionKey
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning !")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    speak("I am your Assistant, Sir. I'm here to help you")


def takeCommand():  # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipwdia....')
            query = query.replace("wikipwdia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open Amazon' in query:
            webbrowser.open("amazon.in")
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open bg' in query:
            webbrowser.open("https://www.google.com/search?q=bibhanshu+gupta&source=lmns&bih=663&biw=1366&rlz=1C1CHWL_enIN997IN997&hl=en&sa=X&ved=2ahUKEwjklbTWmcT4AhUY7nMBHSFrCQwQ_AUoAHoECAEQAA")
        


        elif 'play music' in query:
            music_dir = 'D:\\python_class\\songs'
            songs = os.listdir(music_dir)
            print(random.choice(songs))
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is{strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)









# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('bgupta10cu12@gmail.com', 'Bibhu@2099')
#     server.sendmail('bgupta10cu12@gmail.com', to, content)
#     server.close()




        # elif 'mail' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "bibhanshug72@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry. I am not able to send this email")
