from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

def test_greeting_ok():
    with DockerContainer('rest-service-2025:latest') as container:
        delay = wait_for_logs(container, 'Tomcat started on port')
        driver = webdriver.Remote(command_executor='http://localhost:4444', options=Options())

        driver.get(f'http://{container.get_docker_client().bridge_ip(container._container.id)}:8080/greeting')

        rawdata_tab = driver.find_element(By.ID, 'rawdata-tab')
        
        rawdata_tab.click()

        rawmsg = driver.find_element(By.TAG_NAME, 'pre')
        
        assert 'Hello' in rawmsg.text
        sleep(5)

        driver.quit()

