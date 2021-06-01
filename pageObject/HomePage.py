from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@class='btn btn-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

