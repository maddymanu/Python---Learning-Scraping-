#------
# Borrowed from https://github.com/manojmj92/theoatmeal.com-downloader/blob/master/theoatmeal.py
#-----


from bs4 import BeautifulSoup
import urllib
import os
import sys
import logging


dir = os.path.dirname(os.path.abspath(__file__))
oatmealdir = dir + "//OatmealComics"

if not os.path.exists(oatmealdir):
        os.makedirs(oatmealdir)

main_url = "http://theoatmeal.com/comics_pg/page:2"
main_url_opened = urllib.urlopen(main_url)
main_url_response = main_url_opened.read()

soup = BeautifulSoup(main_url_response)
list_of_links = []

for comic_link in soup.find_all("a"):
  all_links = comic_link.get("href")
  split_links = all_links.split("/")
  try:
    if split_links[1]=="comics" and split_links[2]!="":
      if all_links not in list_of_links:
        list_of_links.append(all_links)
  except: pass

# Forming URLs and downloading comics here
for item in list_of_links:
  old_source = item
  new_souce = old_source.replace('/comics/' , 'http://theoatmeal.com/comics/')
  url = new_souce
  opener = urllib.urlopen(url)
  htmltext = opener.read()

  soup = BeautifulSoup(htmltext)
  # printing the title of the webpage
  print soup.title.string

  comicname = soup.title.string
  comicname = comicname.replace('?','')
  comicname = comicname.replace(':','')
  comicname = comicname.replace('*','')
  comicname = comicname.replace('"','')

  comicdir = dir +"//OatmealComics//"+ comicname

  if not os.path.exists(comicdir):
    os.makedirs(comicdir)
  else:
    if not len(os.listdir(comicdir)) == 0:
      # already exits
      continue
    else:
      # donwload comic here
      print "Downloading a new comic:" + comicname


  for img_link in soup.find_all("img"):
    # link for the particular comic.
    src_link = img_link.get('src')
    curr_comic = src_link.split("/")
    if curr_comic[4] == "comics":
      img_page = urllib.urlopen(src_link)
      img_data = img_page.read()
      filename = curr_comic[6]
      filename = filename.replace('?reload' , '')
      path = os.path.join(comicdir , filename)
      with open (path,"wb") as data:
        data.write(img_data)
  print "Downloaded comic " + comicname


















  #ending here
