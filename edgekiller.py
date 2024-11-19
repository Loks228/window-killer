from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Укажите путь к драйверу
service = Service('D:\\Code\\Python\\driveredge\\msedgedriver.exe')
driver = webdriver.Edge(service=service)

# Функция для проверки и закрытия вкладки YouTube Shorts
def check_and_close_youtube_shorts():
    current_url = driver.current_url
    if 'youtube.com/shorts' in current_url:
        driver.close()

# Откройте браузер и перейдите на YouTube
driver.get('https://www.youtube.com')

try:
    while True:
        check_and_close_youtube_shorts()
        time.sleep(300)  # Проверка каждые 5 минут (300 секунд)
except KeyboardInterrupt:
    print("Скрипт остановлен пользователем.")
finally:
    driver.quit()





