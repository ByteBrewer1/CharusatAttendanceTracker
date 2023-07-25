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


driver = webdriver.Chrome(service=service)
driver.get("https://charusat.edu.in:912/eGovernance/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)


# Locating the username and password input fields using Selenium's
search = wait.until(EC.presence_of_element_located((By.NAME, "txtUserName")))
search.send_keys(User)
search = wait.until(EC.presence_of_element_located((By.NAME, "txtPassword")))
search.send_keys(Password)
search.send_keys(Keys.RETURN)

# Setting Implicit Wait for WebDriver
driver.implicitly_wait(5)

# Waiting for and Extracting Username Element
Name = wait.until(EC.presence_of_element_located((By.ID, "lnkUsername1")))
print(Name.text)


# Clicking on the "View Time Table" Link
c = driver.find_element(by="id", value="grdGrossAtt_ctl01_lnkRequestViewTT")
actions = ActionChains(driver)
actions.click(c)
actions.perform()

# Clicking on the "footAnnouncement" Element

d = driver.find_element(by="id", value="footAnnouncement")
actions = ActionChains(driver)
actions.click(d)
actions.perform()

# Printing Overall Announcement
Overall = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[@id='lblHeadAnnouncement']"))
)
print(Overall.text)
