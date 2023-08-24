from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

search = input("검색어 입력: ")
print("입력 값: ", search)

# 크롬 브라우저 실행
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/results?search_query="+search)

time.sleep(10)