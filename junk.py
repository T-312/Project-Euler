from selenium import webdriver
import selenium
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
pin = 2836221
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)

for i in range(5):
    driver.get("https://kahoot.it/v2/")

    pinbox = driver.find_element_by_id("game-input")
    pinbox.click()
    pinbox.send_keys(pin)
    pinbox.send_keys(Keys.RETURN)

    time.sleep(0.7)

    nick = driver.find_element_by_id("nickname")
    nick.click()
    nick.send_keys(f"Bot{i}")
    nick.send_keys(Keys.RETURN)

driver.quit()