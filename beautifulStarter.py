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
r = requests.get(url)

soup = BeautifulSoup(r.content)
links = soup.find_all("a")

for link in links:
  if "http" in link:
    print link
