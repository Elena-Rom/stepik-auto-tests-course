from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
try:
    browser= webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    find_sum = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(find_sum)

finally:
    time.sleep(10)
    browser.quit()