# Scrapish
from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Out
# from json import dump
import pickle
from dotenv import dotenv_values

ENV = dotenv_values()

driver = webdriver.Chrome()
# display.Image("cc")
driver.get("https://mbasic.facebook.com/login")
# Login phase
current_url = driver.current_url
e = driver.find_element(By.CSS_SELECTOR, "input[name=email]")
p = driver.find_element(By.CSS_SELECTOR, "input[name=pass]")
e.send_keys(ENV.get("FB_USER"))
p.send_keys(ENV.get("FB_PASS"))
driver.find_element(By.CSS_SELECTOR, "input[name=login]").click()
WebDriverWait(driver, 15).until(EC.url_changes(current_url))

pickle.dump(driver.get_cookies(), open("cookies.pickle", "wb"))

print("dumpfs cookie.pickle, keep it safe")