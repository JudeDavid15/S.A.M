import pyttsx3 as ts
import os
import datetime
import speech_recognition as sr
from app import *
from fileopen import *
from news import *

r=sr.Recognizer()
engine=ts.init()
engine.setProperty("rate",150)
cwd=os.getcwd()

def inaudiable():
    engine.say(f"Sorry master {glb_name} i was unable to hear you. Can you repeat it again?")
    engine.runAndWait()
    
def listen():
    
    with sr.Microphone() as source:
        try:
            r.energy_threshold=10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening")
            audio=r.listen(source)
            text=r.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            inaudiable()
            return ""

def date_time(text):
    x=datetime.datetime.now()
    if "time" in text:
        h=x.strftime("%I %M %p")
        engine.say(h)
    elif "day" in text:
        h=x.strftime("%A")
        engine.say(h)
    elif "date" in text:
        h=x.strftime("%d %B %Y")
        engine.say(h)
    elif "year" in text:
        h=x.strftime("%Y")

#info abt the system
def info_sam():
    engine.say("greetings, I am SAM, your personal assistant. SAM stands for Smart Artifical Machine. i can help you open apps or search songs in the internet. I can do more but just not at the moment ")
    engine.runAndWait()
# get your name
def name():
    engine.say("may i know your name")
    engine.runAndWait()
    global glb_name
    glb_name=listen()
    


#greeting
def greetings():
    engine.say(f"Greetings master {glb_name}, SAM online. how can i help you today?")
    
    
#tell current working directory
def current_dir():
    engine.say(f"youre working in {cwd}")

#menu exit command
def exit_command():
    engine.say(f"at your service Master Jude!")
    engine.say("SAM shutting down")
    
def newsinput():
    engine.say("how many articles would you like to know?")
    engine.runAndWait()
    n=int(listen())
    news_reading(n)    

def menu_run(menu):
    if "directory" in menu:
        current_dir()
        engine.runAndWait()

    elif "yourself" in menu:
        info_sam()

    elif "date" in menu or "time" in menu:
        engine.say("what do you wanna know Master jude? the day, or the time or, the month")
        engine.runAndWait()
        date_or_day=listen()
        
        date_time(date_or_day)
        engine.runAndWait()
        # date_time()
        # engine.runAndWait()
    elif "application" in menu:
        engine.say("what app do you wanna open?")
        engine.runAndWait()
        choice=listen()
        appopen(choice)
        
    elif "file" in menu:
        engine.say("where does the file exist master jude?")
        engine.runAndWait()
        fileloc=listen()
        engine.say("what file do you wanna open Master jude?")
        engine.runAndWait()
        fname=listen()
        engine.say("whats the file type Master jude?")
        engine.runAndWait()
        ftype=listen()
        cdrive(fileloc,fname,ftype)

    elif "say news" in  menu:
        newsinput()

    elif menu=="exit" or menu=="bye" or menu=="shutdown":
        exit_command()
        engine.runAndWait()
        return False
    
    else:
        engine.say("I didnt understand that master jude")
        engine.runAndWait()
    return True
        

################################ main block#########################################
name()
greetings()
engine.runAndWait()
running=True

while running:
    engine.say("How can i help you today Master Jude?")
    engine.runAndWait()
    menu=listen().lower()
    if menu=="":
        continue
    running=menu_run(menu)
