import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # 无头模式
    options.add_argument("--nosandbox") #ci环境必须
    options.add_argument("--disable-dev-shm-usage") #ci环境必须
    options.add_argument("--window-size=1920,1080") #设置窗口大小
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield driver
    driver.quit()