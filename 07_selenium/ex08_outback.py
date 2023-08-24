from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.outback.co.kr/menu/productView.do?cateIdx=49&pdtIdx=10314&menuIdx=43")

time.sleep(5)
outback_names = driver.find_elements(By.CSS_SELECTOR, '[class="/main.do?menuIdx="]')

for title in outback_names:
    print(title.text)
