from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.degreesymbol.net/")
link = browser.find_element_by_link_text("» Degree symbol examples")
link.click()

time.sleep(5)
browser.quit()

