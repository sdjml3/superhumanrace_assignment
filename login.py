from selenium.webdriver.common.by import By
class Automation:
    def __init__(self,driver):
        self.driver=driver
    def open(self):
        self.driver.get("https://www.greendash.app/manage-team")
    def user_id(self,userid):
        self.driver.find_element(By.NAME,"name").send_keys(userid)
    def password(self,user_password):
        self.driver.find_element(By.NAME,"password").send_keys(user_password)
    def click_login(self):
        self.driver.find_element(By.NAME,"loginBtn").click()