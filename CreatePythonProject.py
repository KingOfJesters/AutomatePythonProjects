#!/usr/bin/env python3
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path

# file_name = sys.argv[1]
# path = Path('C:/myprojects/pythonprojects')
# os.chdir(path)
# Path(sys.argv[1]+'.py').touch()
file_name = sys.argv[1]
path = Path('C:/myprojects/pythonprojects')
os.chdir(path)
Path(sys.argv[1]).mkdir()
path = Path('C:/myprojects/pythonprojects/'+ sys.argv[1])
os.chdir(path)
Path(sys.argv[1]+'.py').touch()


browser = webdriver.Chrome()
browser.get("https://github.com/login")
python_button = browser.find_element_by_xpath("//*[@id='login_field']")
python_button.send_keys("email@example.com")
python_button = browser.find_element_by_xpath("//*[@id='password']") 
python_button.send_keys("password")
python_button = browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]")
python_button.click()

browser.get("https://github.com/new")
python_button = browser.find_element_by_xpath("//*[@id='repository_name']")
python_button.send_keys(file_name)
python_button = browser.find_element_by_xpath("//*[@id='repository_description']")
python_button.send_keys('this is a python project created automatically')
python_button = browser.find_element_by_xpath("//*[@id='repository_visibility_private']")
python_button.click()
python_button = browser.find_element_by_xpath("//*[@id='repository_auto_init']")
python_button.click()
python_button = browser.find_element_by_css_selector('button.first-in-line')
python_button.submit()