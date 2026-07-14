# Project: Image Site Downloader.
import sys, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_term = sys.argv[1]

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get(f"https://imgur.com/search?q={search_term}")

wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))

images = driver.find_elements(By.TAG_NAME, "img")

count = 0
for img in images:
    src = img.get_attribute("src")
    if src and src.startswith("http") and "avatar" not in src:
        try:
            response = requests.get(src)
            filename = f"image_{count}.jpg"
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"Downloaded: {filename}")
                count += 1
        except Exception as e:
            print(f"Download Error: {e}")

driver.quit()
print(f"Done, all Downloaded: {count} images")
