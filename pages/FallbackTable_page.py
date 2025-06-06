from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FallbackTable:
    def __init__(self,context):
        self.driver=context.driver
        self.setting_sidebar_locator='//ul[@class="metismenu"]//a[@href="#"]'
        self.fallback_table_sidebar_locator='//span[text()="Fallback Table"]'

        self.min_roundrip_list='//input[@name="milesMin"]'
        self.max_roundtrip_list= '//input[@name="milesMax"]'
        self.dollars_per_mile_list='//input[@name="perMile"]'

    def open_fallback_table_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.setting_sidebar_locator)))
        action = ActionChains(self.driver)
        settings_sidebar=self.driver.find_element(By.XPATH, self.setting_sidebar_locator)
        action.move_to_element(settings_sidebar).click().perform()
        fallback_table_sidebar=self.driver.find_element(By.XPATH, self.fallback_table_sidebar_locator)
        action.move_to_element(fallback_table_sidebar).click().perform()

    def fetch_dollar_per_mile_for_roundtrip_miles(self,avg_roundtripmiles):

        min_roundtrips_in_row= self.driver.find_elements(By.XPATH, self.min_roundrip_list)
        min_roundtrip_in_row=[]
        for entry in min_roundtrips_in_row:
            min_roundtrip_in_row.append(round(float(entry.get_attribute("value")),2))
        # print(min_roundtrip_in_row)

        max_roundtrips_in_row=self.driver.find_elements(By.XPATH, self.max_roundtrip_list)
        max_roundtrip_in_row = []
        for entry in max_roundtrips_in_row:
            max_roundtrip_in_row.append(round(float(entry.get_attribute("value")),2))
        # print(max_roundtrip_in_row)

        dollars_per_mile_in_row=self.driver.find_elements(By.XPATH, self.dollars_per_mile_list)
        dollars_per_miles_in_row = []
        for entry in dollars_per_mile_in_row:
            dollars_per_miles_in_row.append(round(float(entry.get_attribute("value")),2))
        # print(dollars_per_miles_in_row)

        get_dollar_per_miles=0.00
        for i in range (len(min_roundtrip_in_row)):
            if min_roundtrip_in_row[i] <= avg_roundtripmiles and avg_roundtripmiles <= max_roundtrip_in_row[i]:
                get_dollar_per_miles= get_dollar_per_miles + dollars_per_miles_in_row[i]

        return get_dollar_per_miles

