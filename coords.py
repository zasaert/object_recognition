from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установите путь к драйверу браузера (например, chromedriver.exe)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу Google Maps
driver.get('https://www.mapcrunch.com/')

count = 800

time.sleep(1)
kys = driver.find_element(By.ID,'hidemainad')
kys.click()

options = driver.find_element(By.ID,'options-button')
options.click()

options = driver.find_element(By.LINK_TEXT,'Ukraine')
options.click()

options = driver.find_element(By.LINK_TEXT,'Germany')
options.click()

options = driver.find_element(By.LINK_TEXT,'Poland')
options.click()

options = driver.find_element(By.LINK_TEXT,'France')
options.click()

search_button = driver.find_element(By.ID,'urban-label')
search_button.click()

search_button = driver.find_element(By.ID,'tour')
search_button.click()


options = driver.find_element(By.ID,'options-button')
options.click()

search_button = driver.find_element(By.ID,'go-button')
element = driver.find_element(By.TAG_NAME,'canvas')

compass= driver.find_element(By.CLASS_NAME,'gm-compass')

i=0
while i <= count:
    time.sleep(2)
    location = element.location
    size = element.size
    screenshot = Image.open(BytesIO(driver.get_screenshot_as_png()))
    element_screenshot = screenshot.crop((0, 80, 1200, 800))
    screenshot_path = f'E:\dataset\street_view_screenshot_{i}.png'
    element_screenshot.save(screenshot_path)
    time.sleep(2)
    search_button.click()
    time.sleep(2)    
    location = element.location
    size = element.size
    screenshot = Image.open(BytesIO(driver.get_screenshot_as_png()))
    element_screenshot = screenshot.crop((0, 80, 1200, 800))
    screenshot_path = f'E:\dataset\street_view_screenshot_{i+1}.png'
    element_screenshot.save(screenshot_path)
    time.sleep(2)
    i+=1

# закрываем браузер
driver.quit()
