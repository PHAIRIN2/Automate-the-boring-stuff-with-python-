import webbrowser

webbrowser.open("http://inventwithpython.com")

import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))

res.status_code = requests.codes.ok

print(len(res.text))

print(res.text[:250])

try:
    res.raise_for_status()
except Exception as exc:
    print("Ther was a problem: %s" % (exc))


# Saving download files to the hard drive.

# res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# res.raise_for_status()
# playfile = open("RomeoAndJuliet.txt", "wb")
# for chunk in res.iter_content(100000):
#   playfile.write(chunk)

# playfile.close()

# HTML.
# Creating a BeautifulSoup object from HTML.
import bs4, requests

res = requests.get("http://nostarch.com")
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))

exampleFile = open("/Users/index.html")
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))

# finding Element with the select() Method
exampleFile = open("/Users/index.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select("#author")
print(type(elems))
print(len(elems))  # result 1
print(elems[0])
print(elems[0].getText())  # result Ai
print(elems[0].attrs)  # result {"id": "author"}

# The selenium Module.

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://www.python.org")

from selenium.webdriver.common.by import By

search_box = driver.find_element(By.ID, "main_container")

search_box.send_keys("authomate the boring stuff")
search_box.submit()
# or
button = driver.find_element(By.ID, "submit-btn")
button.click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located(By.ID, "result"))
driver.quit()

# example
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium python tutorial")
search_box.submit()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

print("Done")
driver.quit
