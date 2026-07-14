# Project: command line emailer.
import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

to_address = sys.argv[1]
message_text = sys.argv[2]

MY_EMAIL = "pp22@gmail.com"
MY_PASSWORD = "wen"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://mail.google.com")

email_field = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email_field.send_keys(MY_EMAIL)
driver.find_element(By.ID, "identifierNext").click()

password_field = wait.until(EC.presence_of_element_located((By.NAME, "passwd")))
time.sleep(1)
password_field.send_keys(MY_PASSWORD)
driver.find_element(By.ID, "passwordNext").click()

compose_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='write']"))
)
compose_btn.click()

to_field = wait.until(EC.presence_of_element_located((By.NAME, "to")))
to_field.send_keys(to_address)

body_field = driver.find_element(By.XPATH, "//div[@aria-label='cats']")
body_field.send_keys(message_text)

send_btn = driver.find_element(By.XPATH, "//div[text()='send']")
send_btn.click()

print("Done")
time.sleep(2)
driver.quit()
