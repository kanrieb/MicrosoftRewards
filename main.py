from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import json
from random import seed
from random import random
from random import randint
import sys

if __name__ == '__main__':
    search_iterations = 31

    firefox_options = Options()
    firefox_options.add_argument("--headless")

    # Mobile
    profile = webdriver.FirefoxProfile()
    if(sys.argv[0] == "--mobile"):
        search_iterations = 21
        profile.set_preference(
            "general.useragent.override", "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")

    # Get login details from JSON
    loginDets = open('login.json', "r")
    parseLogin = json.loads(loginDets.read())
    loginDets.close()

    # go to the Microsoft login page and log in
    driver = webdriver.Firefox(options=firefox_options,
                               executable_path='/Users/kathrynrieb/Projects/MicrosoftRewards/node_modules/geckodriver/geckodriver', firefox_profile=profile)

    driver.get("https://login.live.com/")

    try:
        # Input user name
        w = WebDriverWait(driver, 10)
        time.sleep(3)
        # Wait for username input to load
        w.until(expected_conditions.presence_of_element_located(
            (By.ID, 'i0116')))
        driver.find_element(By.ID, "i0116").send_keys(parseLogin["username"])
        w.until(expected_conditions.presence_of_element_located(
            (By.ID, 'idSIButton9')))
        driver.find_element(By.ID, "idSIButton9").click()

        # Input password
        time.sleep(3)
        w.until(expected_conditions.presence_of_element_located(
            (By.ID, 'i0118')))
        driver.find_element(By.ID, "i0118").send_keys(parseLogin["password"])
        w.until(expected_conditions.presence_of_element_located(
            (By.ID, 'idSIButton9')))
        driver.find_element(By.ID, 'idSIButton9').click()

        # Stay signed in
        time.sleep(3)
        w.until(expected_conditions.presence_of_element_located(
            (By.ID, 'idSIButton9')))
        driver.find_element(By.ID, 'idSIButton9').click()
        # driver.find_element(By.CLASS_NAME, 'idSIButton9').send_keys(Keys.ENTER)

        # Buffer time to sign in
        time.sleep(3)

        driver.get("https://www.bing.com/search?q=porque")
        time.sleep(5)
        driver.get("https://www.bing.com/search?q=round")

        # Run a loop of queries
        start = randint(0, 965)
        url = "https://www.bing.com/search?q="

        file = open("words.txt")
        all_lines = file.readlines()

        for i in range(search_iterations):
            term = all_lines[start+i].strip()
            driver.get(url+term)
            time.sleep(1)

    except TimeoutException:
        print("Timeout happened no page load")
        driver.close()

    driver.close()
