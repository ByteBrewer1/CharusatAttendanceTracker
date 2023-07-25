# AUTHOR :: RAHUL MISTRY
# DATE   :: 25 / 07 / 2023

# importing selenium and getpass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import getpass


User = input("Enter Your Enrollment Number: ")
Password = getpass.getpass("Enter Your Password: ")
PATH = "/path/to/chromedriver"
service = Service(PATH)

