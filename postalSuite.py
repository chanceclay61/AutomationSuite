from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\chanc\PycharmProjects\Automation\drivers\chromedriver.exe")
driver.get("https://store.usps.com/store/home")

driver.find_element_by_id("login-register-header").click()
driver.implicitly_wait(10)
driver.find_element_by_id("username").send_keys(("chanceclay61"))
driver.find_element_by_id("password").send_keys("Chance0176!")
driver.find_element_by_id("btn-submit").click()

# test commit number 2