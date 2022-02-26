from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import sys


def main_function():
    if test_score_service():
        return sys.exit(0)
    else:
        print("Error!")
        return sys.exit(-1)


def test_score_service():
    url = "http://127.0.0.1:8777"
    directory = os.path.dirname(os.path.realpath(__file__))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(executable_path=os.path.join(directory, 'chromedriver'), options=chrome_options)
    chrome_driver.get(url)
    select_score = chrome_driver.find_element(By.XPATH, '//*[@id="score"]').text
    number = select_score

    if int(number) in range(1, 1001):
        return True
    else:
        chrome_driver.close()
        return False

    
main_function()
