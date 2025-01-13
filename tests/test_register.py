from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_register(self):
        try:
            name = "Test User"
            email = "testingmang@example.com"
            password = "password123"

            self.driver.get("http://localhost:3000/")

            register_button = self.driver.find_element(By.LINK_TEXT, "Register")
            register_button.click()
            time.sleep(2)

            register_form = self.driver.find_element(By.CSS_SELECTOR, ".register-container")
            self.assertTrue(register_form.is_displayed(), "Form Register tidak ditemukan!")
            print("✅ Halaman Register berhasil ditemukan.")

            name_input = self.driver.find_element(By.NAME, "name")
            email_input = self.driver.find_element(By.NAME, "email")
            password_input = self.driver.find_element(By.NAME, "password")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            name_input.send_keys(name)
            email_input.send_keys(email)
            password_input.send_keys(password)
            submit_button.click()
            time.sleep(2)
            print("✅ Register berhasil")
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()