from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Admin/Desktop/Pranav/automation/chromedriver.exe"

print("Hello World!")
print("Which web-application do you want to open?")
app = input('Search: ')

if app == 'amazon':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.amazon.in/")
	import amznsearch.py as amazon

if app == 'Amazon':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.amazon.in/")
	import amznsearch.py as amazon

if app == 'youtube':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.youtube.com")
	import ytsearch.py as ytsearch

if app == 'YouTube':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.youtube.com")
	import ytsearch.py as ytsearch

if app == 'instagram':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.instagram.com/")

if app == 'Instagram':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.instagram.com/")

if app == 'insta':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.instagram.com/")

if app == 'Insta':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.instagram.com/")

if app == 'Facebook':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.facebook.com/")

if app == 'facebook':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.facebook.com/")

if app == 'FaceBook':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.facebook.com/")

if app == 'gmail':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.gmail.com")

if app == 'Gmail':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.gmail.com")

if app == 'GMail':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.gmail.com")

if app == 'Google mail':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.gmail.com")

if app == 'google mail':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.gmail.com")

if app == 'Google Mail':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.gmail.com")