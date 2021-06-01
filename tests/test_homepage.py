import pytest
from selenium import webdriver

from ExcelDemoPackage.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self):
        log = self.getlogger() #accessing the logger object
        log.info("msg")
        homePage = HomePage(self.driver)
        homePage.getname().send_keys("testname")
        homePage.getemail().send_keys("test@test.com")
        homePage.getcheckbox().click
        homePage.getsubmit().click
        self.driver.refresh()




