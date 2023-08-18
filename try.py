# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
#
#
# '''
# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
# '''
#
# # driver.get("https://www.amazon.com/Nintendo-Switch-Model-Legend-Zelda-Kingdom/dp/B0BZK5M9TD/?_encoding=UTF8&pd_rd_w=tjgs4&content-id=amzn1.sym.58147189-3d12-4879-b5b2-45824b5b5141&pf_rd_p=58147189-3d12-4879-b5b2-45824b5b5141&pf_rd_r=M15ECVRANHV2YGH3HPVP&pd_rd_wg=4elJX&pd_rd_r=7ba1cfb3-18e9-4710-a345-68963945ca25&ref_=pd_gw_bmx_gp_sg38393n")
# # price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# # print(price.text)
#
# # driver.get("https://www.python.org/")
# # search_bar = driver.find_element(By.NAME, "q")
# # print(search_bar)
# # print(search_bar.tag_name)  # input tag
# # print(search_bar.get_attribute("placeholder"))  # Search
#
# # logo = driver.find_element(By.CLASS_NAME, "python-logo")
# # print(logo.size)
#
# # documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# # print(documentation_link.text)
#
# # bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# # print(bug_link.text)
#
# # events_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# # events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
#
# # event_dict = {}
# # for i in range(len(events_time)):
# #     event_dict[i] = {
# #         "time": events_time[i].text,
# #         "name": events_name[i].text
# #     }
# #
# # print(event_dict)
#
# # driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_cnt = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_cnt = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # print(article_cnt.text)
# # article_cnt.click()
#
# # wikipedia = driver.find_element(By.LINK_TEXT, "Wikipedia")
# # wikipedia.click()
#
# # search = driver.find_element(By.NAME, "search")
# # search.send_keys("Python")
# # search.send_keys(Keys.ENTER)
#
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
# # english = driver.find_element(By.ID, "langSelect-EN")
# # english.click()
# cookie = driver.find_element(By.ID, "cookie")
#
# while True:
#     cookie.click()

for i in range(7, -1, -1):
    print(i)