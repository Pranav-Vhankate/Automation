from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Admin/Desktop/Pranav/automation/chromedriver.exe"
driver = webdriver.Chrome(PATH)

print("What do you want to watch on YouTube?")
watchonyt = input('Search: ')

search = driver.find_element_by_class_name("search_query")
search.send_keys("{}".format(watchonyt))

click = driver.find_element_by_id("search-icon-legacy")
click.click()