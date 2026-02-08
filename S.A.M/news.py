import requests
import json
import urllib.request
import pyttsx3 as ts
engine=ts.init()
apikey = "507032c4a9fc44c406390b9f46e8e8b6"
url = f"https://gnews.io/api/v4/search?q=example&lang=en&max=10&apikey={apikey}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]
    
    def news_reading(n):
         for i in range(n):
            # articles[i].title
            print(f"Title: {articles[i]['title']}")
            engine.say(f"Title: {articles[i]['title']}")
            engine.runAndWait()
             # articles[i].description
            engine.say(f"Description: {articles[i]['description']}")
            engine.runAndWait()
            print(f"Description: {articles[i]['description']}")
   