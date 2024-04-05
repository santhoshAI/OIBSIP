import pyttsx3 as tts
from decouple import config
import keyboard as kb
import os
from datetime import datetime as dt
import speech_recognition as sr
import requests
from list import list 
import online_fun as of
import info 


user_name = info.user
bot =  info.bot
map_api = info.map_api



eng = tts.init()
eng.setProperty('volume', 0.8)
eng.setProperty('rate', 150)
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[0].id)

def say(text):
    
    eng.say(text)
    eng.runAndWait()


def voice_recog():
    
    recog = sr.Recognizer()
    with sr.Microphone() as mic:
        say("I am lisening")
        print("lisening...")
        recog.pause_threshold = 1
        audio = recog.listen(mic)
            
    try:  
        print("Recognizion...")
        query = recog.recognize_google(audio, language='en-in').lower()
                                    
    except Exception:
        say("Sorry I couldn't understand, please repeat that?")
        voice_recog()
        query = 'None'
    
    return query


def greet():
    
    hour = dt.now().hour
    if (hour >= 6) and (hour < 12):
        say("Good Morning")        
    elif (hour >= 12) and (hour < 16):
        say("Good Afternoon")        
    elif (hour >= 16) and (hour < 18):
        say("Good Evening")        
    elif (hour >= 18) and (hour < 24):
        say("Hello")
    
    say(f"I am {bot}, Your Virtual Assistant. How can I assist you {user_name}.")
    


def opening_file(query):
    
    if ("open" in query) and ("power" in query) or ("toys" in query):
        app = query.split().index("open")
        app = query.split()[app+1]
        of.powertoys_search(app)
        
    elif ("minimize" in query) and ("windows" in query):
        of.minimize()
        
    elif ("intro" in query) or ("introduce" in query):
        say("I'm an AI digital assistant created by santhosh. My main function is to assist users like you by providing information, opening application, answering questions, and engaging in conversations on various topics.")
        
    elif ("whatsapp" in query) and ("open" in query):
        say(f"i am working on it {user_name}")
        os.startfile("C:\\Users\\SANTHOSH\\OneDrive\\Desktop\\WhatsApp.exe - Shortcut.lnk")
        say("Opening Whatsapp")  
              
    elif ("powerpoint" in query) and ("open" in query):
        say(f"i am working on it {user_name}")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        say("opening powerpoint") 
               
    elif ("youtube" in query) and ("open" in query):
        say(f"i am working on it {user_name}")
        os.startfile("C:\\Users\\SANTHOSH\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\YouTube.lnk")
        say("oping youtube")
        
    elif ("ip address" in query) and ("tell" in query or "say" in query):
        say(f"i am working on it {user_name}")
        ip_address = of.find_ip()
        say(f"your ip address is {ip_address}")
       
    elif ('wikipedia' in query) and ("search" in query):
        say(f"i am working on it {user_name}")
        say("what do you want to seach on wikipedia ?")
        query = voice_recog()
        result = of.wikipedia_search(query)
        say(result)
        
    elif ('youtube' in query) and ('search' in query):
        say(f"i am working on it {user_name}")
        say("what do you want to search on youtube ?")
        query = voice_recog()
        of.youtube_search(query)
    
    elif ('google' in query) and ('search' in query):
        say(f"i am working on it {user_name}")
        say("what do you want to search on google ?")
        query = voice_recog()
        of.google_search(query)
    
    elif('gmai' in query or 'email') and ('send' in query):
        say(f"i am working on it {user_name}")
        say(f'on what email address do you want to send {user_name}?. please enter in the terminal')
        receiver_email = input("Enter Email Address: ")
        say(f"what should be the subject {user_name}?. just say")
        subject = voice_recog().capitalize()
        say(f"{user_name} say message centent")
        message = voice_recog().capitalize()
        
        if of.send_mail(receiver_email, subject, message):
            say(f"I have sent the email {user_name}")
        else:
            say(f"something went wrong please check the error {user_name}.")
    
    elif ('news' in query):
        say(f"i am working on it {user_name}")
        say(f"I am reading out the latest news of today, {user_name}")
        news = of.news()
        for i in news:
            say(i)
        say(f"I print that in screen {user_name}")
        print(*news, sep="\n")
        
    elif ('weather' in query):
        say(f"i am working on it {user_name}")
        ip = of.find_ip()
        city = requests.get(f"https://api.geoapify.com/v1/ipinfo?apiKey={map_api}").json()
        city_name = city['city']['name']
        say(f"getting weather report of your city {city_name}")
        weather, temp, feel_like = of.weather(city_name)
        say(f"The weather in {city_name} is {temp} and {weather}. Due to humidity, it feels like {feel_like}.")
        print(f"The weather in {city_name} is {temp} and {weather}. Due to humidity, it feels like {feel_like}.")
        
    elif ('calculate' in query):
        say(f"i am working on it {user_name}")
        result = of.calculation(query)
        say(result)
        print(result)
        
    elif ('what' in query) or ('which' in query) or ('who' in query) or ('where' in query) or ('when' in query):
        say(f"i am working on it {user_name}")
        result = of.question(query)
        say(result)
        print(result)
        
    else:
        say(f"Sorry {user_name}, i can't do that")


lisen = True

def Start_Listening():
    global lisen
    lisen = True
    print("Start lisen")

def Stop_Listening():
        global lisen
        lisen = False
        print("Stop lisen")
        
kb.add_hotkey('ctrl+alt+k', Start_Listening)
kb.add_hotkey('ctrl+alt+p', Stop_Listening)

                    

def start():
    
    while True:
        if lisen:
            query = voice_recog()
            if not 'stop' in query or 'exit' in query:
                opening_file(query)
                  
            else:                   
                say(f"oky {user_name}, Take care {user_name}")
                exit()


if __name__ == '__main__':
    greet()
    start()