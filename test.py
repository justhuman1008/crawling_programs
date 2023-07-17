import discord #pip install discord #기본 pip
import asyncio #pip install asyncio #기본 pip
from urllib.request import urlopen #실검파싱
import urllib #실검파싱
from urllib.request import Request, urlopen
import urllib.request #실검파싱
from bs4 import BeautifulSoup #실검파싱



url = "https://search.naver.com/search.naver?query=KRW+JPY"
html = urlopen(url)
parse = BeautifulSoup(html, "html.parser")
tags = parse.find("span", {"class" : "spt_con dw"}).get_text()
result = tags.replace(" ","")
inline1 = result.find("수") + 1
inline2 = result.find("전")
exchange_rate = result[inline1:inline2]

inline3 = result.find("비") + 3
changed = result[inline3:]

print(result)
print(exchange_rate)
print(changed)
