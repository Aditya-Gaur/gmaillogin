from selenium import webdriver
import time

driver = webdriver.Chrome('E:\\python_work\\WebDrivers\\chromedriver.exe')

gmail = 'IT"S YOUR CHOICE @gmail.com'
passward = 'PASSWORD'

driver.get("https://www.gmail.com")
time.sleep(3)

driver.find_element_by_id("identifierId").send_keys(gmail)
time.sleep(2)
driver.find_element_by_id("identifierNext").click()
time.sleep(2)
driver.find_element_by_name("password").send_keys(passward)
time.sleep(2)
driver.find_element_by_id("passwordNext").click()
