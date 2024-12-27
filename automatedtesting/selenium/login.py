# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions

# ToDo: Add more functional UI tests as per your requirements. 
def add_all_products_to_cart(driver):
    print("Adding all products to the cart.")
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        product.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    print("All products added to the cart.")
    time.sleep(5)


def remove_all_products_from_cart(driver):
    print("Removing all products from the cart.")
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
    time.sleep(2)
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    for item in cart_items:
        item.find_element(By.CLASS_NAME, "cart_button").click()
    print("All products removed from the cart.")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    print("Logging in...")
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    
    print("Login successful.")
    add_all_products_to_cart(driver)
    time.sleep(2)
    remove_all_products_from_cart(driver)
    
    print("Test completed successfully.")
    driver.quit()

if __name__ == "__main__":
    main()
