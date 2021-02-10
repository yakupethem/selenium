from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url="http://github.com"
driver.get(url)
driver.maximize_window()

searchInput=driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(1)

result=driver.find_elements_by_css_selector(".v-align-middle")
for element in result:
    print(element.text)

#driver.close()