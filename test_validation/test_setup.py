from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep

options = Options()
options.binary_location = '/home/gael/Projects/argonaultes/2025-2026/epsi-paris-i2-dete933/browsers/chrome-linux64/chrome'
service = Service(executable_path='/home/gael/Projects/argonaultes/2025-2026/epsi-paris-i2-dete933/browsers/chromedriver-linux64/chromedriver')

driver = webdriver.Chrome(options=options, service=service)

driver.get('https://www.selenium.dev/selenium/web/web-form.html')

sleep(10)

driver.quit()

