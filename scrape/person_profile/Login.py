from selenium import webdriver


class Login:
    urlBase = "https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def go(self):
        driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        driver.get(self.urlBase)
        emailButton = driver.find_element_by_id("username")
        passwordButton = driver.find_element_by_id("password")
        emailButton.send_keys(self.email)
        passwordButton.send_keys(self.password)
        login = driver.find_element_by_css_selector("button.btn__primary--large")
        login.click()
        return driver
