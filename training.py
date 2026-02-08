# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%d %b %Y"))
# import os
# whole_dir=os.walk(r"C:\Users\acer")
# for i,j,k in whole_dir:
#     pass
#     # for file in k
    
from news import *
def newsinput():
    engine.say("how many articles would you like to know?")
    engine.runAndWait()
    n=int(input("enter the number"))
    news_reading(n)
newsinput()

    
