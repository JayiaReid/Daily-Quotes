# This is a daily quotes automation mini project

# web scrapping modules
import calendar
from bs4 import BeautifulSoup 
import requests

# regulation modules
import time
from datetime import datetime

# noftication module
from winotify import Notification, audio


# web scraping
def getQuotes():
        page = requests.get('https://quotes.toscrape.com/')
        soup = BeautifulSoup(page.text, "html.parser")
        quotes = soup.findAll("span", attrs={"class":"text"})
        queue = []
        for quote in quotes:
            queue.append(quote.text)
        
        return queue
    
def notify(quote):
    iconImg = "C:/Users/jayia/OneDrive/Documents/Programming/Python Projects/Daily Quotes/bouquet-of-flowers.png"
    alert = Notification(app_id="Quotes4U", 
                     title="Quote of the day",
                     msg=quote,
                     duration="long",
                     icon=iconImg)
    alert.show()
    


def main():
    quotes = getQuotes()
    
    while True:
        
        now = time.time()
        
        nextDay = now + (calendar.timegm(time.gmtime()) + 86400) % 86400
        time.sleep(nextDay-now)
        
        if not quotes:
            quotes = getQuotes()
             
        notify(quotes.pop(0))
        
        
if __name__ == "__main__":
    main()
        

    
