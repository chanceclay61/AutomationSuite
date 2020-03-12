from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome("drivers\chromedriver.exe")


def login():

    driver.get("https://store.usps.com/store/home")
    driver.find_element_by_id("login-register-header").click()
    time.sleep(15)  # will remove once automation is no longer blocked on login

    # driver.find_element_by_id("username").send_keys("chanceclay61")
    # driver.find_element_by_id("password").send_keys("Chance0176!")
    # driver.find_element_by_id("btn-submit").click()
    # driver.find_element_by_id("mail-ship-width").click()


def main_navigation():

    # navigate to schedule pickup
    action = ActionChains(driver)
    first_level_menu = driver.find_element_by_id('mail-ship-width')
    action.move_to_element(first_level_menu).perform()
    second_level_menu = driver.find_element_by_xpath('//*[@id="g-navigation"]/div/nav/ul/li[2]/div/ul[1]/li[4]/a')
    second_level_menu.click()

    # click Check Availability button
    driver.find_element_by_id('webToolsAddressCheck').click()

    # delivery location drop down selector
    select_location = Select(driver.find_element_by_id('packageLocation'))
    time.sleep(3)  # need to refactor to wait for element
    select_location.select_by_value('Front_Door')

    # delivery time radio button selector
    driver.find_element_by_css_selector("input[type='radio'][id='pickup-specific-time']").click()

    # select time drop down selector
    select_time = Select(driver.find_element_by_id('puodSelectTime'))
    time.sleep(3)  # need to refactor to wait for element
    select_time.select_by_value('10:00:00')

    # select calendar date
    driver.find_element_by_xpath('//*[@id="schedule-pickup-cal"]/div/div[2]/table/tbody/tr[4]/td[4]/a').click()  # need
    # to refactor to dynamically find clickable date

    # Input number of packages for Priority Mail Express
    driver.find_element_by_id('countPriorityExpress').send_keys(1)

    # Input package weight
    driver.find_element_by_id('totalPackageWeight').send_keys(1)

    # Check Terms and Conditions checkbox
    driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/div/div[3]/label/input').click()

    # Click Schedule a Pickup button
    driver.find_element_by_id('schedulePickupButton').click()

    # Click Checkout button
    time.sleep(3)  # need to refactor to wait for element
    driver.find_element_by_id('atg_store_checkout').click()


def main():

    login()
    main_navigation()
    # driver.quit()


main()
