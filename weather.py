#import json to load json data to python dictionary

import json

#urllib.request to make a request to api

import urllib.request

city=input("enter city : ")

''' api key might be expired use your own api_key
    place api_key in place of appid="your api_key here "  '''

#source contain json data from api

source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

#converting json data to dictionary

list_of_data=json.loads(source)

#printing data for variable list_of_data
print(" ")
print("country code : ",list_of_data['sys']['country'])
print("coordinate : ",list_of_data['coord']['lon']," ",list_of_data['coord']['lat'])
print("temp : ",list_of_data['main']['temp'],'k'," \npressure : ",list_of_data['main']['pressure']," \nhumidity : ",list_of_data['main']['humidity'])

