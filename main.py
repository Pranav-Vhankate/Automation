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
	import amznsearch.py as amazon

if app == 'Amazon':
	import amznsearch.py as amazon

if app == 'youtube':
	import ytsearch.py as ytsearch

if app == 'YouTube':
	import ytsearch.py as ytsearch

if app == 'instagram':
	import insta_search as ig

if app == 'Instagram':
	import insta_search as ig

if app == 'insta':
	import insta_search as ig

if app == 'Insta':
	print("Processing...")
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.instagram.com/")

if app == 'Facebook':
	import insta_search as ig

if app == 'facebook':
	import fb_search as fb

if app == 'FaceBook':
	import fb_search as fb

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
