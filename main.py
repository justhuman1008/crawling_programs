import discord
from os import listdir
from setting import token, want_int, userID

# 크롤링
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

bot = discord.Bot()

@bot.event # 봇 작동
async def on_ready():
    print("=========================")
    print("아래의 계정으로 로그인 : ")
    print(bot.user.name)
    print("연결에 성공했습니다.")
    print("=========================")
    await bot.change_presence(activity=discord.Game("/가이드"))

for filename in listdir('./cogs'): # Cogs 자동 로드(봇 작동시)
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]}가 정상적으로 로드되었습니다.')


@bot.slash_command(description="현재 엔화 환율 확인")
async def 환율(ctx):
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
        if result.find("하락") == "-1":
            updown = "상승"
        else:
            updown = "하락"
        print(exchange_rate)
        print(changed)
        plm = exchange_rate.replace(".","")
        reach = discord.Embed(title=f"현재 환율", description=f"­", colour=0xffdc16)
        reach.add_field(name=f"현재 환율", value=f"{exchange_rate}\n{updown} {changed}\n\n[네이버 환율 바로가기](https://search.naver.com/search.naver?query=KRW+JPY)", inline=False)
        reach.set_thumbnail(url="https://logoproject.naver.com/img/img_story_renewal.png")
        await ctx.respond(embed=reach)

bot.run(token)