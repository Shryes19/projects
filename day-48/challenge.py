from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

k = driver.find_element(By.NAME, value="fName")
k.send_keys("Shryes")
k = driver.find_element(By.NAME, value="lName")
k.send_keys("M")
k = driver.find_element(By.NAME, value="email")
k.send_keys("shryes107@gmail.com")

send = driver.find_element(By.CSS_SELECTOR,value=".form-signin button")
send.click()