from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Admin/Desktop/Pranav/automation/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.amazon.in/")