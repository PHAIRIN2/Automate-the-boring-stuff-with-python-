# Project: 2048 Bot.
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/")

time.sleep(2)

body = driver.find_element(By.TAG_NAME, "body")
body.click()
time.sleep(1)

moves = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]
time.sleep(1)
try:
    while True:
        for move in moves:
            body.send_keys(move) 
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Programmed")
    driver.quit()