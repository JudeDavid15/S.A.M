from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class info:
    def __init__(self):
        self.driver=webdriver.Chrome(service=Service("C:\Program Files\Google\Chrome\Application\chrome.exe"))
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
assistance=info()
assistance.get_info("spiders")