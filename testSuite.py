from AutomationSuite.postalSuite import login, login_failure, login_success, main_navigation, credit_card_success, \
    browser
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def successful_login_test():

    login(browser)
    login_success(browser)


def incorrect_credentials_login_test():

    login(browser)
    login_failure(browser)


def visa_credit_authentication_test():

    login(browser)
    main_navigation(browser)
    credit_card_success(browser)


def mastercard_credit_authentication_test():

    login(browser)
    main_navigation(browser)
    credit_card_success(browser)


def american_express_credit_authentication_test():

    login(browser)
    main_navigation(browser)
    credit_card_success(browser)


def discover_credit_authentication_test():

    login(browser)
    main_navigation(browser)
    credit_card_success(browser)


def main():

    successful_login_test()
    incorrect_credentials_login_test()
    visa_credit_authentication_test()
    mastercard_credit_authentication_test()
    american_express_credit_authentication_test()


main()


