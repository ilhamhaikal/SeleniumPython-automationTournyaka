from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_forget_password():
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Data email
        email = "testingmang@example.com"

        # Buka halaman utama
        driver.get("http://localhost:3000/")

        # Klik tombol Login dulu
        login_button = driver.find_element(By.LINK_TEXT, "Login")
        login_button.click()
        time.sleep(2)

        # Klik tombol Forget Password
        forget_password_link = driver.find_element(By.LINK_TEXT, "Forget Password")
        forget_password_link.click()
        time.sleep(2)

        # Verifikasi halaman Forget Password
        forget_password_form = driver.find_element(By.CSS_SELECTOR, ".login-container")
        assert forget_password_form.is_displayed(), "Form Forget Password tidak ditemukan!"
        print("✅ Halaman Forget Password berhasil ditemukan.")

        # Isi email
        email_input = driver.find_element(By.NAME, "email")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_input.send_keys(email)
        submit_button.click()
        time.sleep(2)
        print("✅ Reset password berhasil dikirim")

    finally:
        # Tutup browser
        driver.quit()