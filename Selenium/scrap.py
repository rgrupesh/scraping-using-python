from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/login?")

username = driver.find_element_by_id("username")
username.send_keys("laxokir101@gridmauk.com")

password = driver.find_element_by_id("password")
password.send_keys("XXX")

driver.find_element_by_xpath('//button[text()="Sign in"]').click()

driver.get("https://www.google.com.np/")

query = driver.find_element_by_name("q")
query.send_keys('site:linkedin.com/in/ AND "deep learning"')
query.send_keys(Keys.RETURN)








