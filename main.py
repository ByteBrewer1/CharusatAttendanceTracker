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


# Store the data in text file
def store_attendance_data(user_name, att_data):
    file_name = f"{user_name}_attendance.txt"
    with open(file_name, "w") as file:
        file.write("Attendance Data for: " + user_name + "\n\n")
        for c_data in att_data:
            file.write("Course: " + c_data["Course"] + "\n")
            file.write("Class Type: " + c_data["Class Type"] + "\n")
            file.write("Total: " + c_data["Total"] + "\n")
            file.write("Percentage: " + c_data["Percentage"] + "\n")
            file.write("--------------------------------------\n")


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


print("-------------------------------------------------")

# Course 1:
Course1 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl02_lblSubjct']")
    )
)
print("Course = ", Course1.text)

Class1 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl02_lblClass']")
    )
)
print("Class Type = ", Class1.text)

Total1 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[2]/td[3]",
        )
    )
)
print("Total = ", Total1.text)

Percentage1 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[2]/td[4]",
        )
    )
)
print("Percentage = ", Percentage1.text)

print("-------------------------------------------------")

# Course 2:
Course2 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl03_lblSubjct']")
    )
)
print("Course = ", Course2.text)

Class2 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl03_lblClass']")
    )
)
print("Class Type = ", Class2.text)

Total2 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[3]/td[3]",
        )
    )
)
print("Total = ", Total2.text)

Percentage2 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[3]/td[4]",
        )
    )
)
print("Percentage = ", Percentage2.text)

print("-------------------------------------------------")

# Course 3:
Course3 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl04_lblSubjct']")
    )
)
print("Course = ", Course3.text)

Class3 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl04_lblClass']")
    )
)
print("Class Type = ", Class3.text)

Total3 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[4]/td[3]",
        )
    )
)
print("Total = ", Total3.text)

Percentage3 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[4]/td[4]",
        )
    )
)
print("Percentage = ", Percentage3.text)

print("-------------------------------------------------")

# Course 4:

Course4 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl05_lblSubjct']")
    )
)
print("Course = ", Course4.text)

Class4 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl05_lblClass']")
    )
)
print("Class Type = ", Class4.text)

Total4 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[5]/td[3]",
        )
    )
)
print("Total = ", Total4.text)

Percentage4 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[5]/td[4]",
        )
    )
)
print("Percentage = ", Percentage4.text)

print("-------------------------------------------------")

# Course 5:

Course5 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl06_lblSubjct']")
    )
)
print("Course = ", Course5.text)

Class5 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='grdGrossAtt_ctl06_lblClass']")
    )
)
print("Class Type = ", Class5.text)

Total5 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[6]/td[3]",
        )
    )
)
print("Total = ", Total5.text)

Percentage5 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
            "2]/table[1]/tbody[1]/tr[6]/td[4]",
        )
    )
)
print("Percentage = ", Percentage5.text)

print("-------------------------------------------------")

# Course 6:

Course6 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl07_lblSubjct']")
    )
)
print("Course = ", Course6.text)

Class6 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl07_lblClass']")
    )
)
print("Class Type = ", Class6.text)

Total6 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[7]/td[3]",
        )
    )
)
print("Total = ", Total6.text)

Percentage6 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[7]/td[4]",
        )
    )
)
print("Percentage = ", Percentage6.text)

print("-------------------------------------------------")

# Course 7:

Course7 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl08_lblSubjct']")
    )
)
print("Course = ", Course7.text)

Class7 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl08_lblClass']")
    )
)
print("Class Type = ", Class7.text)

Total7 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[8]/td[3]",
        )
    )
)
print("Total = ", Total7.text)

Percentage7 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[8]/td[4]",
        )
    )
)
print("Percentage = ", Percentage7.text)

print("-------------------------------------------------")

# Course 8:

Course8 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl09_lblSubjct']")
    )
)
print("Course = ", Course8.text)

Class8 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl09_lblClass']")
    )
)
print("Class Type = ", Class8.text)

Total8 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[9]/td[3]",
        )
    )
)
print("Total = ", Total8.text)

Percentage8 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[9]/td[4]",
        )
    )
)
print("Percentage = ", Percentage8.text)

print("-------------------------------------------------")

# Course 9:

Course9 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl10_lblSubjct']")
    )
)
print("Course = ", Course9.text)

Class9 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@id='gvGrossAttPop_ctl10_lblClass']")
    )
)
print("Class Type = ", Class9.text)

Total9 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[10]/td[3]",
        )
    )
)
print("Total = ", Total9.text)

Percentage9 = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div["
            "1]/div[1]/table[1]/tbody[1]/tr[10]/td[4]",
        )
    )
)
print("Percentage = ", Percentage9.text)

print("-------------------------------------------------")

# Extracting and converting username to string
UserName = str(Name.text)

# Converting course, class, and total attendance details to strings
str_Course1 = str(Course1.text)
str_Class1 = str(Class1.text)
str_Total1 = str(Total1.text)

str_Course2 = str(Course2.text)
str_Class2 = str(Class2.text)
str_Total2 = str(Total2.text)

str_Course3 = str(Course3.text)
str_Class3 = str(Class3.text)
str_Total3 = str(Total3.text)

str_Course4 = str(Course4.text)
str_Class4 = str(Class4.text)
str_Total4 = str(Total4.text)

str_Course5 = str(Course5.text)
str_Class5 = str(Class5.text)
str_Total5 = str(Total5.text)

str_Course6 = str(Course6.text)
str_Class6 = str(Class6.text)
str_Total6 = str(Total6.text)

str_Course7 = str(Course7.text)
str_Class7 = str(Class7.text)
str_Total7 = str(Total7.text)

str_Course8 = str(Course8.text)
str_Class8 = str(Class8.text)
str_Total8 = str(Total8.text)

str_Course9 = str(Course9.text)
str_Class9 = str(Class9.text)
str_Total9 = str(Total9.text)

attendance_data = []
course_num = 1

# Looping until there are no more courses to extract
while True:
    try:
        # Using dynamic XPaths with the help of course_num to locate each course's details
        course = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//span[@id='grdGrossAtt_ctl{str(course_num + 1).zfill(2)}_lblSubjct']",
                )
            )
        )
        class_type = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//span[@id='grdGrossAtt_ctl{str(course_num + 1).zfill(2)}_lblClass']",
                )
            )
        )
        total = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div["
                    f"2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                    f"2]/table[1]/tbody[1]/tr[{str(course_num + 1)}]/td[3]",
                )
            )
        )
        percentage = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div["
                    f"2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                    f"2]/table[1]/tbody[1]/tr[{str(course_num + 1)}]/td["
                    f"4]",
                )
            )
        )

        # Storing the extracted data in a dictionary for the current course
        course_data = {
            "Course": course.text,
            "Class Type": class_type.text,
            "Total": total.text,
            "Percentage": percentage.text,
        }

        # Adding the course_data dictionary to the attendance_data list
        attendance_data.append(course_data)

        # Incrementing course_num to move to the next course for the next iteration
        course_num += 1

    except:
        # Break the loop when there are no more courses to extract (an exception is raised)
        break

# Store the attendance data in a text file in the current working directory
store_attendance_data(User, attendance_data)

driver.quit()
