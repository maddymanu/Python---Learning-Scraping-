import urllib2
import json

def fullContact(email):
  api_key = '59e857091a56241e'
  email = email
  fullCURL = 'https://api.fullcontact.com/v2/person.json?apiKey=' + api_key +'&email='+email
  loadURL = urllib2.urlopen(fullCURL)
  data = json.load(loadURL)
  print data
  photos = data['photos']

  for item in photos:
    print item['url']

fullContact('maddymanu@hotmail.com')
