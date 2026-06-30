from pages.login_page import LoginPage  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert page.get_product_title() == "Products"

def test_login_failed(driver):
    page = LoginPage(driver)
    page.open()
    page.login("111","222")
    error_message = page.wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    assert "Username and password do not match" in error_message.text