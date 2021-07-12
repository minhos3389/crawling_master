# 금붕어 웹툰 활용 예시

import requests 
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=723790"
res = requests.get(url)
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text()
# print(title)

# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# # 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 가져오기
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 :", total_rates)
print("평균 점수 :", (total_rates / len(cartoons)))