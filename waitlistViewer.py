from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import getpass
import os

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
driver = webdriver.Chrome(service_args=["--verbose"])

driver.get("https://mytritonlink.ucsd.edu")

elem = driver.find_element_by_name("urn:mace:ucsd.edu:sso:username")
elem.send_keys(usr)
elem = driver.find_element_by_name("urn:mace:ucsd.edu:sso:password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm#tabs-crs")

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
currElem.submit()

# btn = getElem("socFacSubmit")
# btn.send_keys("\n")
# btn.click()
# btn.click()


# html_source = driver.page_source
# driver.quit()

# soup = BeautifulSoup(html_source,'html.parser')
# soup.prettify()
# tables = soup.find_all("table" , recursive=False)
# print tables
