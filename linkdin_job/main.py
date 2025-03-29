from selenium import webdriver
from selenium.webdriver.common.by import By
import time

num = "6362799465"
# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&trk=public_jobs_conversion-modal-signin&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3989642624%26f_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom")

email = driver.find_element(By.ID, value="username")
email.send_keys("shryesPython19@gmail.com")
password = driver.find_element(By.ID, value="password")
password.send_keys("shryes@19")
sign_in = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
sign_in.click()

easy_apply = driver.find_element(By.XPATH, value='//*[@id="ember47"]/span')
easy_apply.click()

ph_num = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989642624-4565986378-phoneNumber-nationalNumber"]')
ph_num.send_keys(num)

n = driver.find_element(By.ID, value="ember392")
n.click()