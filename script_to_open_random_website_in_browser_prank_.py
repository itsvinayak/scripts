import webbrowser
import time
import random


while True:
    sites=random.choice(['google.com','fb.com','iert.in'])
    visit="http://{}".format(sites)
    webbrowser.open_new(str(visit))
    seconds=random.randrange(5,20)
    time.sleep(seconds)
