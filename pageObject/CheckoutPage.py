from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import FinalPage


class CheckOutPage:
    cardTitle = (By.CSS_SELECTOR , ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//*[contains(@class,'nav-link btn btn-primary')]")
    confirmtext = (By.XPATH, "//a[text()= 'Blackberry']")
    confirmpurchase = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkoutbutton(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def confirmproduct(self):
        return self.driver.find_element(*CheckOutPage.confirmtext)

    def ConfirmPurchase(self):
        self.driver.find_element(*CheckOutPage.confirmpurchase).click()
        finalpage = FinalPage(self.driver)
        return finalpage



