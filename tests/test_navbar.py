from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestNavbar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_navbar(self):
        try:
            self.driver.get("http://localhost:3000/")
            time.sleep(2)
            navbar = self.driver.find_element(By.CSS_SELECTOR, "nav.navbar")
            self.assertTrue(navbar.is_displayed(), "Navbar tidak ditemukan!")
            print("✅ Navbar berhasil ditemukan.")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            raise e

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()