import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# select_one로 하나의 영화명 갖고오기
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# scrapping 하고 싶은 부분에서 Copy - Copy Selector 붙여넣

print(title)
print(title['href']) # title의 속성값
print(title.text) # title의 text값

print('='*30)

# select로 모든 영화명 갖고오기
trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        title = a_tag.text
        print(title)