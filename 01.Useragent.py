# Useragent

# 403 에러나는 경우 : 권한문제
# 웹사이트에 접속하는 user의 정보를 사이트는 알 수 있습니다.
# 웹사이트에 주는 header 정보에 따라 주고자하는 정보를 선택할 수 있습니다.
# 사람이 아닌 컴퓨터가 크롤링을 위해 접근할 경우 서버 부하문제가 발생하므로, 이를 차단하는 경우가 있습니다.

import requests 

url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# 위에서 정의한 header 값을 같이 전송
res = requests.get(url, headers=headers)
res.raise_for_status() 

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)