import requests
from bs4 import BeautifulSoup
import random
import os
import sys
from appscript import *
import subprocess

# fileName = sys.argv[1]
# app('Finder').desktop_picture.set(mactypes.File(fileName))

dir = os.path.dirname(os.path.abspath(__file__))
# print dir

someecardsdir = dir +"\\Someecards"

url = 'http://www.someecards.com/ecards/all/?sort=newest'
r = requests.get(url)
soup = BeautifulSoup(r.content)

img_data = soup.find_all("div" , {"class" : "img-wrapper"})
curr_img_data = random.choice(img_data)


img_url = curr_img_data.find_all("img")[0].get("src")
print img_url
