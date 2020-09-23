from selenium import webdriver
import time


PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/login?")

username = driver.find_element_by_id("username")
username.send_keys("laxokir101@gridmauk.com")

password = driver.find_element_by_id("password")
password.send_keys("XXX")

driver.find_element_by_xpath('//button[text()="Sign in"]').click()

time.sleep(50)

driver.quit()





