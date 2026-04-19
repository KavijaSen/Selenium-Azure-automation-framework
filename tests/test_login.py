import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in login_page.get_flash_message()