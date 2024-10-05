from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def scrape_images(search_term, max_images):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.google.com/search?q={search_term}&tbm=isch")

    def scroll_to_end():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 

    image_urls = set()
    while len(image_urls) < max_images:
        scroll_to_end()
        thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
        
        for img in thumbnails[len(image_urls):]:
            try:
                img.click()
                time.sleep(1) 
                actual_images = driver.find_elements(By.CSS_SELECTOR, "img.n3VNCb")
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))
            except Exception as e:
                print(f"Error al procesar una imagen: {e}")

            if len(image_urls) >= max_images:
                break

    driver.quit()
    return list(image_urls)[:max_images]