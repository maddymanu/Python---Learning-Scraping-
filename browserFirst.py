import mechanize
import cookielib
from bs4 import BeautifulSoup
import html2text
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


br = mechanize.Browser()
#
# cj = cookielib.LWPCookieJar()
# br.set_cookiejar(cj)
#
# # Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
#
# # Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#
# # User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
# Use this to login to mytritonlink.
br.open('https://mytritonlink.ucsd.edu')

# br.open('https://github.com/login')

# Inspect name of the form
for f in br.forms():
    print f

# change to match the number
# br.select_form(nr=0)

# Login
# br.submit()
# time.sleep(10)

# print(br.open('https://mytritonlink.ucsd.edu').read())

print "Enter Your Username please"
usr = raw_input(">>>>>")

print "Enter Your Password please"
pwd = raw_input(">>>>>")


chromedriver = "/Users/adityabansal/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
# webdriver.Chrome(chromedriver)
driver = webdriver.Chrome(service_args=["--verbose"])

driver.get("https://mytritonlink.ucsd.edu")

elem = driver.find_element_by_name("urn:mace:ucsd.edu:sso:username")
elem.send_keys(usr)
elem = driver.find_element_by_name("urn:mace:ucsd.edu:sso:password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.get("https://act.ucsd.edu/studentAcademicHistory/academichistorystudentdisplay.htm")
html_source = driver.page_source
driver.quit()


soup = BeautifulSoup(html_source,'html.parser')
print soup


















#
