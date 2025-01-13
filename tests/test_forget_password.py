from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestForgetPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_forget_password(self):
        try:
            email = "testingmang@example.com"
            self.driver.get("http://localhost:3000/")

            login_button = self.driver.find_element(By.LINK_TEXT, "Login")
            login_button.click()
            time.sleep(2)

            forget_password_link = self.driver.find_element(By.LINK_TEXT, "Forget Password")
            forget_password_link.click()
            time.sleep(2)

            forget_password_form = self.driver.find_element(By.CSS_SELECTOR, ".login-container")
            self.assertTrue(forget_password_form.is_displayed(), "Form Forget Password tidak ditemukan!")
            print("✅ Halaman Forget Password berhasil ditemukan.")

            email_input = self.driver.find_element(By.NAME, "email")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            email_input.send_keys(email)
            submit_button.click()
            time.sleep(2)
            print("✅ Reset password berhasil dikirim")
        except Exception as e:
            print(f"❌ Test failed: {str(e)}")
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()