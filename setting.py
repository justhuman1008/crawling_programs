import os

# 봇 기본정보
token = os.environ['Token'] # 봇의 토큰
guild = int(os.environ['Guild']) # 테스트용(관리자 전용) 길드

#원하는 환율 설정 ---------------------------------------------------------------------------------------

userID = int(os.environ['userID'])
channelID = int(os.environ['channelID'])
want_int = 90500 #뒤에 00 붙이기