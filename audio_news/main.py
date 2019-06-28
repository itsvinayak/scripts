import pyttsx3
import requests
import json
import time

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=7c43977c018a4fab95f8e7ab3aa7e710')
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)

sound=engine.getProperty ('voices');
engine.setProperty('voice','sound[1].id')


try:
    response = requests.get(url)
except:
    engine.say("can,t access link , plz check you internet ")

news=json.loads(response.text)


for new in news['articles']:
    print("##############################################################\n")
    print(str(new['title']),"\n\n")
    engine.say(str(new['title']))
    print('______________________________________________________\n')
    engine.runAndWait()
    print(str(new['description']),"\n\n")
    engine.say(str(new['description']))
    engine.runAndWait()
    print("..............................................................")
    time.sleep(2)
