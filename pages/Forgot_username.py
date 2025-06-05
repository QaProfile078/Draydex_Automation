from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotUsername:
    def __init__(self,context):
        self.driver= context.driver
        self.forgot_username_button='//a[text()="Forgot Username?"]'
        self.forgot_username_heading_locator ='//h3[@class="text-center heading"]'
        self.get_username_button_locator= '//button[@type="submit"]'

        self.require_field_locator='//div[@class="invalid-feedback"]'
        self.error_messages_locator='//p[@class="error_msg_style"]'

        self.email_field_locator_on_forgot_username_page='//input[@placeholder="Enter your email address"]'
        self.dot_number_field_on_forgot_username_page='//input[@placeholder="Enter DOT number"]'
        self.address_field_locator_on_forgot_username='//input[@placeholder="Company Address"]'
        self.usertype_radiobutton_locator='//input[@name="user_type" and @id="customer"]'

        self.dot_number_verification_loader='//p[@class="dot_msg error_msg_style"]'

    def click_on_forgot_username(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.forgot_username_button)))
        forgot_username_button=self.driver.find_element(By.XPATH, self.forgot_username_button)
        return forgot_username_button.click()

    def is_forgot_username_heading_on_the_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.forgot_username_heading_locator)))
        forgot_username_heading= self.driver.find_element(By.XPATH, self.forgot_username_heading_locator)
        return forgot_username_heading.text == "Forgot Username"

    def click_on_get_username_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.get_username_button_locator)))
        action= ActionChains(self.driver)
        get_username_button= self.driver.find_element(By.XPATH, self.get_username_button_locator)
        return action.move_to_element(get_username_button).click().perform()

    def error_messages_present_under_required_field(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.error_messages_locator)))
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.require_field_locator)))
        all_error_and_required_field_messages=[]
        required_fields=self.driver.find_elements(By.XPATH, self.require_field_locator)
        for message_element in required_fields:
            all_error_and_required_field_messages.append(message_element.text)
        error_message= self.driver.find_elements(By.XPATH,self.error_messages_locator)
        for message_element in error_message:
            all_error_and_required_field_messages.append(message_element.text)

        print(all_error_and_required_field_messages)
        return all_error_and_required_field_messages

    def fill_email_id_field_on_forgot_username_page(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.email_field_locator_on_forgot_username_page)))
        email_id=self.driver.find_element(By.XPATH,self.email_field_locator_on_forgot_username_page)
        return  email_id.send_keys("testcust1702@yopmail.com")

    def fill_dot_number_field_on_forgot_username_page(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.dot_number_field_on_forgot_username_page)))
        dot_number= self.driver.find_element(By.XPATH, self.dot_number_field_on_forgot_username_page)
        return dot_number.send_keys(1523020)

    def fill_company_address_field_on_forgot_username_page(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.address_field_locator_on_forgot_username)))
        address="60139"
        for digit in address:
            self.driver.find_element(By.XPATH, self.address_field_locator_on_forgot_username).send_keys(int(digit))

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="city-listing-css"]')))
        assert address in self.driver.find_element(By.XPATH, '//ul[@class="city-listing-css"]//div').text
        return self.driver.find_element(By.XPATH, '//ul[@class="city-listing-css"]//div').click()

    def select_customer_usertype(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.usertype_radiobutton_locator)))
        customer_radio_button= self.driver.find_element(By.XPATH, self.usertype_radiobutton_locator)
        return customer_radio_button.click()

    def wait_for_dot_verification(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.dot_number_verification_loader)))
        dot_number_message=self.driver.find_element(By.XPATH,self.dot_number_verification_loader)
        return dot_number_message.text == ""

