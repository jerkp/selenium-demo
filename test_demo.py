import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://www.saucedemo.com")

    wait = WebDriverWait(driver, 10)
    #username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
    # username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    # username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    # username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#user-name")))]")))
    # username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']"))))
    username_input.send_keys("standard_user")

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    # driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()

    #product_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    product_title = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Products']")))
    assert product_title.text == "Products"
