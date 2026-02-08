import subprocess as sbp
import webbrowser as wb
import pyttsx3 as ts
engine= ts.init()
# for spotify
def spotify():
    song = input("enter the song name: ").replace(" ", "%20")
    wb.open("https://open.spotify.com/search/" + song)

#for amazon
def amazon():
    search=input("what do you wanna buy: ").replace(" ","+")
    wb.open("https://www.amazon.in/s?k=" + search)
    

# for pinterest
def pinterest():
    inspo = input("Enter the inspo you need: ").replace(" ", "%20")
    wb.open("https://in.pinterest.com/search/pins/?q=" + inspo)

def google():
    searchquery=input("What do you wanna search ").replace(" ","+")
    wb.open("https://www.google.com/search?q="+ searchquery)
    
def youtube():
    searchquery=input("What do you wanna search ").replace(" ","+")
    wb.open("https://www.youtube.com/results?search_query="+ searchquery)

def appopen(menu):
    
    app = {
        "chrome": google,
        "notepad": "notepad",
        "files": "file explorer",
        "pinterest":pinterest,
        "spotify":spotify,
        "youtube":youtube,
        "cmd":"command prompt",
        "settings":"settings"
        }
   
    if "google" in menu:
        app["chrome"]()

    elif "chrome" in menu and "app" in menu:
        sbp.Popen(app["chrome"])
    
    elif "youtube" in menu:
            app["youtube"]()

    elif "spotify" in menu:
        app["spotify"]()

    elif "spotify" in menu and "app" in menu:
        sbp.Popen("Spotify")

    elif "pinterest" in menu:
        app["pinterest"]()

    elif "notepad" in menu:
        sbp.Popen(app["notepad"])

    elif "files" in menu:
        sbp.Popen(app["files"])

    elif "cmd" in menu  or "command prompt" in menu or "prompt" in menu:
        sbp.Popen(app["cmd"])

    elif "settings" in menu:
        sbp.Popen(app["settings"])
    
    else:
        print("bye")




# # main code
# while True:
#     if "google" in menu:
#         wb.open("https://www.google.com/")

#     elif "chrome" in menu:
#         sbp.Popen(app["chrome"])

#     # elif "spotify" in menu:
#     #     spotify()

#     elif "spotify" in menu:
#         sbp.Popen("Spotify")

#     elif "pinterest" in menu:
#         pinterest()

#     elif "notepad" in menu:
#         sbp.Popen(app["notepad"])

#     elif "files" in menu:
#         sbp.Popen(app["files"])

#     else:
#         print("bye")
#         break
