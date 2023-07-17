import os

# 봇 기본정보
token = os.environ['Token'] # 봇의 토큰
owner = os.environ['Owner'] # 봇 소유자

guild = int(os.environ['Guild']) # 테스트용(관리자 전용) 길드

#원하는 환율 설정 ---------------------------------------------------------------------------------------

userID = os.environ['userID']
want_int = 90000 #뒤에 00 붙이기