import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import FinalPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")..because in the below line, we have inherited the parent class, this line is not req
class TestOne(BaseClass): #inheritence  of the parent class to child class

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
#        checkoutpage = CheckOutPage(self.driver)
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooters()[i].click()
                checkoutpage.checkoutbutton().click()
        confirmitem = checkoutpage.confirmproduct().text
        assert cardText == confirmitem
        finalpage = checkoutpage.ConfirmPurchase()
#        finalpage = FinalPage(self.driver)
        finalpage.selectcountry().send_keys("ind")
        self.verifylinkpresence("India")
        finalpage.confirmcountry().click()
        finalpage.CheckBox().click()
        finalpage.ButtonSuccess().click()
        final_text = finalpage.AlertSuccess().text
        log.info(final_text)
        assert "Success" in final_text
        self.driver.get_screenshot_as_file("testcase1.png")


