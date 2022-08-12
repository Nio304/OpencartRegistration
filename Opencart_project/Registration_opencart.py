from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class OpenCart():
    def test_login_valid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #Site Link
        driver.get("https://demo.opencart.com/")
        time.sleep(5)
        driver.maximize_window()

        #my account
        my_accout=driver.find_element(By.XPATH,'/html/body/nav/div[2]/div[2]/ul/li[2]/div/a/span')
        my_accout.click()
        time.sleep(5)

        #regestration
        driver.find_element(By.XPATH,'/html/body/nav/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a').click()
        time.sleep(5)

        #First_name_place
        driver.find_element(By.XPATH, '//input[@id="input-firstname"]').send_keys("Niloy")
        time.sleep(5)

        #Last_name_place
        driver.find_element(By.XPATH, '//input[@id="input-lastname"]').send_keys("Newaz")
        time.sleep(5)

        #emial_place
        driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("annniloy@gmail.com")
        time.sleep(5)

        #password_place
        driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("123456789")
        time.sleep(5)

        #Radio_button_click
        driver.find_element(By.XPATH,'//input[@id="input-newsletter-yes"]').click()
        time.sleep(5)

        #I_aggre_term
        driver.find_element(By.XPATH,'//input[@name="agree"]').click()
        time.sleep(5)

        #button_click
        driver.find_element(By.XPATH,'//button[@class="btn btn-primary"]').click()
        time.sleep(5)

        print("Sucessfully Registration")

        time.sleep(5)
        driver.close()

test_obj = OpenCart()
test_obj.test_login_valid()