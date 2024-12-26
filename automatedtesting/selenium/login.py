# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

login('standard_user', 'secret_sauce')

# ToDo: Add more functional UI tests as per your requirements. 
def add_all_products_to_cart(driver):
    print("Adding all products to the cart.")
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        product.find_element(By.CLASS_NAME, "btn_inventory").click()
    print("All products added to the cart.")

def remove_all_products_from_cart(driver):
    print("Removing all products from the cart.")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    for item in cart_items:
        item.find_element(By.CLASS_NAME, "cart_button").click()
    print("All products removed from the cart.")

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    print("Logging in...")
    login(driver, "standard_user", "secret_sauce")
    
    print("Login successful.")
    add_all_products_to_cart(driver)
    time.sleep(2)
    remove_all_products_from_cart(driver)
    
    print("Test completed successfully.")
    driver.quit()

if __name__ == "__main__":
    main()
