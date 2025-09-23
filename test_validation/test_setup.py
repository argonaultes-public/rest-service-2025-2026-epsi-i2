from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
from time import sleep

driver = webdriver.Remote(command_executor='http://localhost:4444', options=Options())

driver.get('https://www.selenium.dev/selenium/web/web-form.html')

sleep(10)

driver.quit()

