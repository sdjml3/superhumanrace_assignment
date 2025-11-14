from selenium.webdriver.common.by import By
import random

class ManageTeamPage:
    def __init__(self,driver):
        self.driver= driver
    def search_user(self,name):
        self.driver.find_elements("xpath",'//button[@data-team_name="Back End Developers"]')[1].click()
        self.driver.find_element(By.NAME,"memberSearch").send_keys(name)
    def select_user(self):
        self.driver.find_element("xpath",'//ul[@id="employer-list"]/li').click()
    def select_role(self):
        role=self.driver.find_elements("xpath",'//input[@class="roleType ml-0 mt-0"]')
        random.choice(role).click()
    def admin_box(self):
        admin=self.driver.find_elements("xpath",'//input[@name="adminAccessType[]"]')
        random.choice(admin).click()
    def save(self):
        self.driver.find_element(By.ID,"saveCorporateTeamMember").click()

    

