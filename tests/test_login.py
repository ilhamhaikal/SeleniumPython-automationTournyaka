from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Data login
        email = "user3@example.com"
        password = "password123"

        # Buka halaman utama
        driver.get("http://localhost:3000/")

        # Klik tombol Login
        login_button = driver.find_element(By.LINK_TEXT, "Login")
        login_button.click()
        time.sleep(2)

        # Verifikasi halaman Login
        login_form = driver.find_element(By.CSS_SELECTOR, ".login-container")
        assert login_form.is_displayed(), "Form Login tidak ditemukan!"
        print("✅ Halaman Login berhasil ditemukan.")

        # Isi form login
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
        time.sleep(2)
        print("✅ Login berhasil")

        # Logout
        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        time.sleep(2)
        print("✅ Logout berhasil")

    finally:
        # Tutup browser
        driver.quit()