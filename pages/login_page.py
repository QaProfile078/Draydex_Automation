
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, context):
        self.driver = context.driver
        self.rms_url = 'https://rms.devtrust.biz/login'
        self.prod_url= 'https://app.draydex.com/login'
        self.uat_url='https://uat.draydex.com/login'
        self.staging_url='https://testing.draydex.com/login'
        self.login_button= '//button[@type="submit"]'
        self.invalid_login_message= '//div[contains(@class, "Toastify__toast-body")]'
        self.username_is_required_message='(//div[@class="invalid-feedback"])[1]'
        self.password_is_required_message='(//div[@class="invalid-feedback"])[2]'

        self.forgot_password_button_locator='//a[contains(text(),"Forgot Password")]'

    def open(self,context):
        if context.server == "uat":
            self.driver.get(self.uat_url)
        if context.server == "staging":
            self.driver.get(self.staging_url)
        if context.server == "prod":
            self.driver.get(self.prod_url)

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def is_error_message_displayed(self):
        try:
            error_message_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.invalid_login_message))
            )

            error_message = error_message_element.text.strip()
            print(f"Error message found: {error_message}")
            return "Login credentials are invalid." in error_message

        except TimeoutException:
            print("Error message did not appear in time or disappeared too quickly.")

    def is_on_login_page(self):
        WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(EC.title_contains("Login"))
        return "Login" in self.driver.title

    def is_username_required_displayed(self):
        try:
            username_required_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.username_is_required_message))
            )

            username_required_message = username_required_element.text.strip()
            print(f"Error message found: {username_required_message}")
            return "The username field is required" in username_required_message
        except TimeoutException:
            print("Username required message did not appear in time")

    def is_password_required_displayed(self):
        try:
            password_required_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.password_is_required_message))
            )

            password_required_message = password_required_element.text.strip()
            print(f"Error message found: {password_required_message}")
            return "The password field is required." in password_required_message
        except TimeoutException:
            print("Password required message did not appear in time")

    def click_on_forgot_password(self):
        forgot_password_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.forgot_password_button_locator)))
        return forgot_password_button.click()