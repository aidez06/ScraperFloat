from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import time
import os
import random

# Set the path to the ChromeDriver executable



class Float:
    driver_path = f"{os.getcwd()}/chromedriver112/chromedriver-windows-x64.exe"
    def __init__(self) -> None:
        # Create a new instance of the Chrome driver
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()


    def authorization(self):
        self.driver.get('URL')
        try:
            login_auth = WebDriverWait(self.driver, 1000).until(
                EC.presence_of_all_elements_located((By.XPATH, '//img[@src="assets/login-steam.png"]'))
            )
            login_auth[random.randint(0,len(login_auth))].click()

            try:
                WebDriverWait(self.driver,5).until(
                    EC.presence_of_element_located((By.XPATH,'//input[@type="text"]'))
                )
            except:
                pass

        except:
            pass
        time.sleep(20000)

f = Float()
f.authorization()