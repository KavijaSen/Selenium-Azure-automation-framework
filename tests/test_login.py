from pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)

    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "secure area" in login.get_message().lower()