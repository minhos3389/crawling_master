import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# lxml parser를 넣어줬습니다.
# 가져온 res.text를 lxml로 parsing한 BeautifulSoup 객체
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
## 문자열만 가져올 수 있습니다.
# print(soup.title.get_text())
## soup객체가 가지고 있는 것 중, 첫번째 a 태그를 가져오라는 명령어
# print(soup.a)

# 어떤 속성을 갖고 있는지 볼 수 있습니다.
# 딕셔너리 형태
# a element의 a 값 정보 출력
# print(soup.a.attrs)
# # href 값만 가져오고자 할때
# # a element의 href 속성 값 정보 출력
# print(soup.a['href'])

# 해당 페이지의 이해도가 낮을 경우 사용하면 좋은 코드
# 조건을 줘서 해당 조건을 만족하는 첫 엘리먼트를 가져옵니다.
# class="Nbtn_upload"인 a element를 찾아줘.
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))

# # ckass-"Nbtn_upload"인 element를 찾아줘.
# print(soup.find(attrs={"class":"Nbtn_upload"}))

# print(soup.find("li", attrs={"class":"rank01"}))

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling) #아무것도 출력x
# print(rank1.next_sibling.next_sibling.get_text()) # 다음 a 태그에 담긴 웹툰제목가져옴.

# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
## 부모 요소 출력
# print(rank1.parent)

# next_sibling으로 가는데 조건에 해당하는 것만 찾습니다.
# li태그인 next_sibling만 찾습니다.
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

## 조건에 해당하는 형제들 모두를 가져옵니다.
# print(rank1.find_next_siblings("li"))

# 해당하는 텍스트의 a태그 가져오기.
# webtoon = soup.find("a", text="윈드브레이커-3부 - 120화 라이트 캐벌리")
# print(webtoon)

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 "a" element 를 반환
for cartoon in cartoons:
    print(cartoon.get_text())

