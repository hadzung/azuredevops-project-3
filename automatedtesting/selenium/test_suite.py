from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import login  # Importing the existing login module

def add_all_products_to_cart(driver):
    print("Adding all products to the cart.")
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        add_to_cart_button = product.find_element(By.CLASS_NAME, "btn_inventory")
        add_to_cart_button.click()
        print(f"Added product: {product.find_element(By.CLASS_NAME, 'inventory_item_name').text}")
    print("All products added to the cart.")

def remove_all_products_from_cart(driver):
    print("Removing all products from the cart.")
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    time.sleep(2)

    # Wait for the cart items to be visible
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    for item in cart_items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        remove_button = item.find_element(By.CLASS_NAME, "cart_button")
        print(f"Removing product: {item_name}")
        remove_button.click()
        # Wait until the item is removed from the cart
        #WebDriverWait(driver, 10).until(EC.staleness_of(item))
    print("All products removed from the cart.")

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    try:
        driver = login.login("standard_user", "secret_sauce")
        
        if driver:
            add_all_products_to_cart(driver)
            # Take a screenshot before attempting to remove items
            driver.save_screenshot('before_removal.png')
            remove_all_products_from_cart(driver)
        else:
            print("Test aborted due to login failure.")
    finally:
        driver.quit()
        print("Test suite execution completed.")
