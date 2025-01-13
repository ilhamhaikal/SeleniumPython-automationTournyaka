from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_register():
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Data test
        name = "Test User"
        email = "testingmang@example.com"
        password = "password123"
        konfirmasi_password = "password123"

        # Buka halaman utama
        driver.get("http://localhost:3000/")

        # Klik tombol Register
        register_button = driver.find_element(By.LINK_TEXT, "Register")
        register_button.click()
        time.sleep(2)

        # Verifikasi halaman Register
        register_form = driver.find_element(By.CSS_SELECTOR, ".register-container")
        assert register_form.is_displayed(), "Form Register tidak ditemukan!"
        print("✅ Halaman Register berhasil ditemukan.")

        # Isi form register
        name_input = driver.find_element(By.NAME, "name")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
        time.sleep(2)
        print("✅ Register berhasil dilakukan")

    finally:
        # Tutup browser
        driver.quit()