from selenium import webdriver
import time

driver = webdriver.Chrome()
url="http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()

url="http://github.com/yakupethem"
driver.get(url)
print(driver.title)
time.sleep(2)

if "yakupethem" in driver.title:
    driver.save_screenshot("yakupethem_github.png")
    driver.back()
time.sleep(2)
driver.close()