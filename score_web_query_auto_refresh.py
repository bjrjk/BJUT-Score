from selenium import webdriver
from selenium.webdriver import ActionChains
import time,base64,os

browser = webdriver.Chrome()
login_URL = "https://webvpn.bjut.edu.cn/"
browser.get(login_URL)

input("Please press Enter after you have successfully logged in and visit grade page...")

try:
    while True:
        time.sleep(10)
        browser.refresh()
finally:
    browser.close()
