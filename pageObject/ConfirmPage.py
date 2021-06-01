from selenium.webdriver.common.by import By


class FinalPage:
    country = (By.CSS_SELECTOR, "input[class*='validate']")
    countryselect = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox checkbox-primary']")
    successbutton = (By.CSS_SELECTOR, "input[class*='btn btn-success btn-lg']")
    successtext = (By.CLASS_NAME, "alert-success")

    def __init__(self,driver):
        self.driver = driver

    def selectcountry(self):
        return self.driver.find_element(*FinalPage.country)

    def confirmcountry(self):
        return self.driver.find_element(*FinalPage.countryselect)

    def CheckBox(self):
        return self.driver.find_element(*FinalPage.checkbox)

    def ButtonSuccess(self):
        return self.driver.find_element(*FinalPage.successbutton)

    def AlertSuccess(self):
        return self.driver.find_element(*FinalPage.successtext)





