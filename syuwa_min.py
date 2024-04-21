# -*- config: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

if __name__=="__main__":
    driver = None
    try:
        options = Options()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        target_url = "https://www.shuwasystem.co.jp/book/9784798068596.html"
        driver.get(target_url)

        result = dict()
        result["title"] = driver.find_element(By.CLASS_NAME, "titleWrap").text
        result["price"] = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[7]/td').text
        result["author"] = driver.find_element(By.CSS_SELECTOR, "#main > div.detail > div.right > table > tbody > tr:nth-child(1) > td > a").text
        result["describe"] = driver.find_element(By.ID, "bookSample").text
        print(result)

    finally:
        if driver:
            driver.quit()
