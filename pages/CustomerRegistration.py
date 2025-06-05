# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# class CustomerRegistration:
#     def __init__(self,context):
#         self.driver=context.driver
#         self.register_now_button_locator='//a[text()="Register Now"]'
#         self.customer_reg_button_locator='//button[text()="Customer"]'
#         self.submit_registeration_button_locator='//button[@type="submit"]'
#         self.empty_fields_error_messages = '//div[@class="invalid-feedback"]'
#
#         self.cloudfare_box_shadow_host='//div[@id="cf-turnstile"]'
#         self.success_message_shadow_host=''
#         self.success_message_locator='span#success-text'
#
#
#     def click_on_register_now_button(self):
#         WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.register_now_button_locator)))
#         Register_Now=self.driver.find_element(By.XPATH, self.register_now_button_locator)
#         return Register_Now.click()
#
#     def click_on_customer_button(self):
#         WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.customer_reg_button_locator)))
#         Customer_button= self.driver.find_element(By.XPATH, self.customer_reg_button_locator)
#         return Customer_button.click()
#
#     def is_customer_registration_displayed_in_title(self):
#         WebDriverWait(self.driver, 10).until(EC.title_contains("Customer Registration"))
#         print(self.driver.title)
#         return "Customer Registration" in self.driver.title
#
#     # def verify_cloudfare_success_message(self):
#     #     WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.cloudfare_box_shadow_host)))
#     #     action =ActionChains(self.driver)
#     #     ShadowHost= self.driver.find_element(By.XPATH,self.cloudfare_box_shadow_host)
#     #     action.move_to_element(ShadowHost).perform()
#     #     ShadowRoot = self.driver.execute_script('return arguments[0].shadowRoot', ShadowHost)
#     #     print(ShadowRoot)
#     #     shadow_host_2 = ShadowRoot.find_element(By.CSS_SELECTOR, '.body')
#     #     shadow_root_2 = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host_2)
#     #     ShadowElement= shadow_root_2.find_element(By.CSS_SELECTOR, self.success_message_locator)
#     #     return  "Success" in ShadowElement
#
#
#     def click_on_register_button_to_submit(self):
#         WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.submit_registeration_button_locator)))
#         Register_button= self.driver.find_element(By.XPATH, self.submit_registeration_button_locator)
#         action = ActionChains(self.driver)
#         return action.move_to_element(Register_button).click().perform()
#
