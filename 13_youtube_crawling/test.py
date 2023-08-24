from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def scroll_fun():
    while True:
        # 스크롤 하기 전 높이
        before_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 현재 높이 만큼 스크롤 내리기
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        # 스크롤 내린 후 높이
        after_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 스크롤 전, 후 높이 비교
        if before_scroll == after_scroll:
            break

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 인기 급 상승 페이지
driver.get("https://www.youtube.com/feed/trending") 
time.sleep(2)
# 제목 요소 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# 제목 저장을 위한 리스트 
title_list = []
# 조회수 저장을 위한 리스트
hits_list = []

# 무한 스크롤 함수 호출
scroll_fun()

for title in titles:
    if title.get_attribute("aria-label") and title.text: # shorts 영상을 걸러내기 위한 조건문
        #aria-label 속성 값 가져오기
        aria_label = title.get_attribute("aria-label") 
        # print(aria_label)
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))
        print("제목", title.text)
        print("조회수", hits)
        # 제목, 조회수를 각각 리스트에 담기
        # append(): 리스트에 데이터를 추가할 때
        title_list.append(title.text)
        hits_list.append(hits)

# 제목, 조회수 리스트 함께 조회
for title, hit in zip(title_list, hits_list):
    print(title, hit)

# 제목, 조회수 리스트가 담긴 딕셔너리
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

result = pd.DataFrame(crawling_result)
# dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig") 
# 조회수 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")

okt = Okt()

#단어와 종류를 분리
# for word, tag in okt.pos(title):
#    print(word, tag)
word_list = []
for title in title_list:
# 명사, 형용사만 따로 출력
    for word, tag in okt.pos(title):
        if tag in ['Noun', 'Adjective']: # 명사와 형용사
            word_list.append(word)

print(word_list)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 워드클라우드 객체 생성
#wc = WordCloud(font_path='malgun', width=400, height=400)

cand_mask = np.array(Image.open('heart.png'))


wordcloud = WordCloud(
    font_path = 'malgun.ttf', # 한글 글씨체 설정
    background_color='white', # 배경색은 흰색으로 
    colormap='rainbow', # 글씨색은 빨간색으로
    mask=cand_mask, # 워드클라우드 모양 설정
).generate_from_frequencies(word_list_count)

# Counter로 분석한 데이터를 워드클라우드로 만들기
#result = wordcloud.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') #x, y축은 필요없으므로 생략
# 결과를 이미지로 출력할 준비
plt.imshow(wordcloud)
# 이미지 출력
plt.show()


