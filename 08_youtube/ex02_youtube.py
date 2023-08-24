from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 페이지 접속
# 접속할 주소 
# driver.get("https://www.youtube.com/")

# 검색결과 페이지에 바로 접속
driver.get("https://www.youtube.com/results?search_query=뉴진스")

# 검색창 접근
search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')

# 검색어 입력
# search_input.send_keys("뉴진스")

# 검색버튼 클릭
# search_button = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# search_button.click()

# 엔터 치기
search_input.send_keys(Keys.RETURN)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
     print(title.text) # innerHTML 값

time.sleep(5)

# https://www.youtube.com/results?search_query=뉴진스

# https://www.youtube.com/results?search_query=르세라핌