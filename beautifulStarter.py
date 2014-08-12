#
#
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#
# print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC

import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/news/entertainment"
url_somecard = "http://www.someecards.com/ecards/flirting/"
r = requests.get(url_somecard)

soup = BeautifulSoup(r.content)
links = soup.find_all("a")

# Use something like this to download all the images from SomeCard
# for link in links:
#   if "http" in link.get("href"):
#     # print link


# for yellowpages, the div tag is post
# V IMPORTANT - DIV Search can have anything you want
g_data = soup.find_all("div" , {"class" : "img-wrapper"})
print g_data
