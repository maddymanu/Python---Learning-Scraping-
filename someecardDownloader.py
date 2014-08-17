from bs4 import BeautifulSoup
import urllib
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Handling the directory #making a new one if not already there
dir = os.path.dirname(os.path.abspath(__file__))
somecarddir = dir + "//Someecards"
if not os.path.exists(somecarddir):
        os.makedirs(somecarddir)


main_url = "http://www.someecards.com/ecards/flirting/?filter=someecards&sort=classics"
main_url_opened = urllib.urlopen(main_url)
main_url_response = main_url_opened.read()

browser = webdriver.Firefox()
browser.get(main_url)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")
no_of_pagedowns = 5


soup = BeautifulSoup(main_url_response)
links = []

#Going through each page
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
    for somecard_link in soup.find_all("a"):
      try:
        href_link = somecard_link.get("href")
        # print href_link #this is printing the href link many times
        split_link = href_link.split("/")
        try:
          if split_link[1] == "flirting-cards":
            # print split_link[1]
            if href_link not in links:
              print href_link
              links.append(href_link)
        except: pass
      except: pass


print links
