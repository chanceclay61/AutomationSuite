from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(r"C:\Users\chanc\PycharmProjects\Automation\drivers\chromedriver.exe")
driver.get("https://store.usps.com/store/home")

driver.find_element_by_id("login-register-header").click()
time.sleep(15)
# driver.find_element_by_id("username").send_keys(("chanceclay61"))
# driver.find_element_by_id("password").send_keys("Chance0176!")
# driver.find_element_by_id("btn-submit").click()
# driver.find_element_by_id("mail-ship-width").click()
...
action = ActionChains(driver)

firstLevelMenu = driver.find_element_by_id('mail-ship-width')
action.move_to_element(firstLevelMenu).perform()
secondLevelMenu = driver.find_element_by_xpath('//*[@id="g-navigation"]/div/nav/ul/li[2]/div/ul[1]/li[1]/a')
action.move_to_element(secondLevelMenu).perform()
secondLevelMenu.click()