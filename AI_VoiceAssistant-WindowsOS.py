import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Loading your AI personal assistant - Sirena 1.0')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Sirena-1.0")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break


        if 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            #type your API KEY Here
            api_key="be40bed70423970d30420a7f50b16e13"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            #taking input "city name" from user
            speak("whats the city name")
            city_name= takeCommand()
            #complete_url variable to store the complete_url address
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            #get methods of requests module retruns respons object
            response = requests.get(complete_url)
            #json method of response object convert json format data into python format data
            #Javascript Object Notion. It is used for transferring data between the server and the client just like XML
            #It is a built-in package in python
            x=response.json()
            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"]!="404":
                #store the value of "main" key in variable y
                y=x["main"]
                #store the value coressponding to the "temp" key of y
                current_temperature = y["temp"]
                #store the value coressponding to the "humidity" key of y
                current_humidiy = y["humidity"]
                #store the value of "weather" key in variable z
                z = x["weather"]
                #store the value coressponding to the "description" key
                #at the 0th index of z
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            #speak(f"the time is {strTime}")
            speak(strTime)
          
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Sirena version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail,predict time,take a photo,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Navya")
            print("I was built by Navya")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")


        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="YGWR3G-JLAQWWT2K8"
            client = wolframalpha.Client('YGWR3G-JLAQWWT2K8')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/s"])

time.sleep(3)
