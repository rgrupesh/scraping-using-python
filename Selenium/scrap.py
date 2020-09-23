from selenium import webdriver

PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://rupeshgelal.com.np/")

print(driver.title)

driver.quit()

