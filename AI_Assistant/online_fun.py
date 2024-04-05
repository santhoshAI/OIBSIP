import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
import wolframalpha
import pyautogui as gui
import info

EMAIL = info.email
PASSWORD = info.email_password

news_api = info.news
weather_api = info.weather
wolframalpha_api = info.wolframalpha

def find_ip():
    id_address = requests.get('https://api.ipify.org?format=json').json()
    return id_address['ip']

def wikipedia_search(query):
    search = wikipedia.summary(query, sentences=2)
    return search

def youtube_search(query):
    kit.playonyt(query)
    
def google_search(query):
    kit.search(query)
    
def news():
    news = []
    result = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={news_api}').json()
    articles = result['articles'][:5] # top articles
    for article in articles:
        news.append(article['title'])
    return news   
    
def send_mail(receiver_mail, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_mail
        email['Subject'] = subject
        email['From'] = EMAIL

        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        print("done")
        s.send_message(email)
        s.close()
        return True
    
    except Exception as E:
        print(E)
        return False
        
def weather(city): 
    rept = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}").json()
    weather = rept["weather"][0]['main']
    temp = rept['main']['temp']
    feels_like = rept['main']['feels_like']
    return weather, f"{temp}°C", f"{feels_like}°C"

def calculation(query):
    client = wolframalpha.Client(wolframalpha_api)
    try:
        ind = query.split().index("calculate")
        text = query.split()[ind+1:]
        result = client.query("".join(text))
        ans = next(result.results).text
        return ans
    except StopIteration:
        return "I couldn't find that. Please try again"
    except:
        return "I couldn't find that. Please try again"
    
def question(query):
    client = wolframalpha.Client(wolframalpha_api)
    try:
        ind = query.split().index("what") if 'what' in query else \
            query.split().index("which") if 'which' in query else \
            query.split().index("who") if 'who' in query else \
            query.split().index("where") if 'where' in query else \
            query.split().index("when") if 'when' in query else None
            
        if ind is not None:
            text = query
            result = client.query(text)
            ans = next(result.results).text
            return ans
        
        else:
            return "I couldn't find that."
    except StopIteration:
        return "I couldn't find that. Please try again"
    
def powertoys_search(app):
    gui.hotkey('win', 'd', interval=0.25)
    gui.hotkey('alt', ' ', interval=0.25)
    gui.write(app, interval=0.25)
    gui.press('enter',interval=0.10)
    
def minimize():
    gui.hotkey('win', 'd', interval=0.25)
    