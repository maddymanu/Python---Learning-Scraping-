from bs4 import BeautifulSoup
import urllib
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
somecarddir = dir + "//Someecards"

if not os.path.exists(somecarddir):
        os.makedirs(somecarddir)

main_url = "http://www.someecards.com/ecards/flirting/?filter=someecards&sort=classics"
main_url_opened = urllib.urlopen(main_url)
main_url_response = main_url_opened.read()

soup = BeautifulSoup(main_url_response)
links = []

for somecard_link in soup.find_all("a"):
  try:
    href_link = somecard_link.get("href")
    # print href_link
    split_link = href_link.split("/")
    try:
      if split_link[1] == "flirting-cards":
        # print split_link[1]
        if href_link not in links:
          links.append(href_link)
    except: pass
  except: pass

print links
