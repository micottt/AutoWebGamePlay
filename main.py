from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

'''
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
'''

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

check_store_time = time.time() + 5

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)

# elements = driver.find_elements(By.CSS_SELECTOR, "#store b")
# prices = []
# for element in elements:
#     if element.text:
#         price = int(element.text.split(" - ")[1].replace(",", ""))
#         prices.append(price)
#         print(price)


while True:
    cookie.click()

    if time.time() > check_store_time:
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        max_price_item = [0, ""]
        elements = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for item_id, element in zip(item_ids, elements):
            if element.text != "":
                item_price = int(element.text.split(" - ")[1].replace(",", ""))
                if money >= item_price > max_price_item[0]:
                    max_price_item = [item_price, item_id]

        purchase_id = max_price_item[1]
        if purchase_id != "":
            item = driver.find_element(By.ID, purchase_id)
            item.click()

        check_store_time = time.time() + 5



