from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from login import Automation
from manage_team_page import ManageTeamPage

options=webdriver.ChromeOptions()
prefs={
    "credentials_enable_service":False,
    "profile.password_manager_leak_detection":False,
    "profile.password_manager_enabled":False
}
options.add_experimental_option("prefs",prefs)
options.add_argument("--disable-notifications")

def role_assignment():
    driver=webdriver.Chrome(options=options)
    login=Automation(driver)
    login.open()

    login.user_id("testing@mysuperhumanrace.com")
    login.password("test@123")

    login.click_login()

    time.sleep(3)

    manage=ManageTeamPage(driver)
    employee_names=["Lisa","Rose","sakshi","Simranjeet"]
    emp_name=random.choice(employee_names)
    manage.search_user(emp_name)
    time.sleep(2)
    manage.select_user()
    manage.select_role()

    manage.save()
    time.sleep(2)
    driver.quit()

try:
    role_assignment()
except Exception as error:
    print(error)
