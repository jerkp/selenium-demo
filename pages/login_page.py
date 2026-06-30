from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):  #每创建一个实例就触发一次这个函数
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def login(self,username,password):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()

    def get_product_title(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))).text