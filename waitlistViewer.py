from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import getpass
import os
import cookielib
import httplib
import socket


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

print bcolors.HEADER
print "Enter Your Username please"
usr = raw_input(">>>>> ")

print "Enter Your Password please"
pwd = getpass.getpass(">>>>> ")
print bcolors.ENDC

chromedriver = "/Users/adityabansal/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(service_args=["--verbose"])
driver = webdriver.Firefox()
# driver.set_page_load_timeout(45)
driver.set_script_timeout(30)
timeout = 30
socket.setdefaulttimeout(timeout)

driver.get("https://mytritonlink.ucsd.edu")

elem = driver.find_element_by_name("urn:mace:ucsd.edu:sso:username")
elem.send_keys(usr)
elem = driver.find_element_by_name("urn:mace:ucsd.edu:sso:password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm#tabs-crs")
parent_h = driver.current_window_handle


# element = driver.find_element_by_id("courses")


def getElem(id):
  try:
      element = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.ID, id))
      )
  finally:
      # element = driver.find_element_by_id("courses")
      return element

currElem = getElem("courses")
course = "CSE 100"
currElem.send_keys(course)




try:
  print currElem.submit()
  print "here"
except:
  print "try1"

while True:
  try :
    driver.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm#tabs-sub")
    break
  except httplib.CannotSendRequest:
    print "Cant Get Google"
  except socket.timeout:
    print "Socket Error"

code_btn = driver.find_elements_by_xpath("//*[contains(text(), 'by code')]")
code_btn[0].click()

currElem = getElem("courses")
currElem.submit()











# Done
