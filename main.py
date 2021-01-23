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
	import insta_search.py as ig

if app == 'Instagram':
	import insta_search.py as ig

if app == 'insta':
	import insta_search.py as ig

if app == 'Insta':
	import insta_search.py as ig

if app == 'Facebook':
	import fb_search as fb

if app == 'facebook':
	import fb_search as fb

if app == 'FaceBook':
	import fb_search as fb

if app == 'gmail':
	import gmail_search.py as gmail

if app == 'Gmail':
	import gmail_search.py as gmail

if app == 'GMail':
	import gmail_search.py as gmail

if app == 'Google mail':
	import gmail_search.py as gmail

if app == 'google mail':
	import gmail_search.py as gmail

if app == 'Google Mail':
	import gmail_search.py as gmail