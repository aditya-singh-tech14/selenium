
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


x_path_LoginButton = '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/form/div[4]/button'


@pytest.fixture(scope="class")
def setup_class(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver  # Assign driver to the class instance
    yield
    driver.quit()



@pytest.mark.usefixtures("setup_class")
class TestLoginNologin():
    def test_mcs_through_feedback_form_shared_mail(self):

        driver = self.driver
        self.driver.get("https://staging-secure.enthu.ai/login")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'email_address').send_keys('aditya+staging2@enthu.ai')
        self.driver.find_element(By.ID, 'password').send_keys('12345678')
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_LoginButton)))
        print("login button found")
        login_button.click()
        time.sleep(3)
