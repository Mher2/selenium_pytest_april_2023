import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://github.com")
time.sleep(2)
