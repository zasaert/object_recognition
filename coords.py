from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Установите путь к драйверу браузера (например, chromedriver.exe)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу Google Maps
driver.get('https://www.mapcrunch.com/')

count = 1000

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
#zoom = driver.find_element(By.XPATH,'/html/body/div[2]/div[6]/div/div/div[13]/div[2]/div[3]/div/button[1]')


search_button.click()  
time.sleep(4) 
i=0
a=0
while i <= count:
    temp = 0
    time.sleep(0.5)
    while temp <= 6:
        location = element.location
        size = element.size
        screenshot = Image.open(BytesIO(driver.get_screenshot_as_png()))
        element_screenshot = screenshot.crop((0, 80, 1200, 800))
        screenshot_path = f'F:\dataset\street_view_screenshot_{i+temp}.png'
        element_screenshot.save(screenshot_path)
        time.sleep(1)
        temp+=1
    search_button.click()   
    i+=6

# закрываем браузер
driver.quit()
