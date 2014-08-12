import urllib2
import json

locu_api = '3b7a5d6539cdb5108fa26468e2d8014aaad1dc95'


def locu_search(query):
  api_key = locu_api
  url = 'https://api.locu.com/v1_0/venue/search/?api_key='+api_key
  locality = query.replace(' ' , "%20")
  finalUrl = url+"&locality=" + locality + "&category=restaurant"
  obj = urllib2.urlopen(finalUrl)
  data = json.load(obj)

  for item in data['objects']:
    print item['name']
    print item['phone']


locu_search('New Delhi')
