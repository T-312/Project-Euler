import selenium, chromedriver_autoinstaller, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

options = Options()
driver = selenium.webdriver.Chrome(chrome_options=options)

driver.get("https://www.mail.com/int/")
time.sleep(3)

for i in range(4):
    driver.send_keys(Keys.TAB)
driver.send_keys(Keys.RETURN)

sign_up = driver.find_element_by_id('signup-button')
sign_up.click()

