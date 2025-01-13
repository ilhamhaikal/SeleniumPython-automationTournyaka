from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        try:
            email = "user3@example.com"
            password = "password123"
            self.driver.get("http://localhost:3000/")
            
            login_button = self.driver.find_element(By.LINK_TEXT, "Login")
            login_button.click()
            time.sleep(2)

            login_form = self.driver.find_element(By.CSS_SELECTOR, ".login-container")
            self.assertTrue(login_form.is_displayed(), "Form Login tidak ditemukan!")
            print("✅ Halaman Login berhasil ditemukan.")

            email_input = self.driver.find_element(By.NAME, "email")
            password_input = self.driver.find_element(By.NAME, "password")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            email_input.send_keys(email)
            password_input.send_keys(password)
            submit_button.click()
            time.sleep(2)
            print("✅ Login berhasil")
        except Exception as e:
            print(f"❌ Error during login: {str(e)}")
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()