# 디스코드 API
import discord
from discord.ext import commands, tasks

# 크롤링
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

# 전역변수
from setting import want_int, userID

#------------------------------------------------------------------------------------------

class exchange_rate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Auto_check.start()

    @tasks.loop(seconds=60)
    async def Auto_check(self):
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
        if int(plm) <= want_int:
            user = await self.bot.fetch_user(userID)
            reach = discord.Embed(title=f"목표 환율에 도달했습니다.", description=f"­", colour=0xffdc16)
            reach.add_field(name=f"현재 환율", value=f"{exchange_rate}\n{updown} {changed}\n\n[네이버 환율 바로가기](https://search.naver.com/search.naver?query=KRW+JPY)", inline=False)
            reach.set_thumbnail(url="https://logoproject.naver.com/img/img_story_renewal.png")
            await user.send(embed=reach)

    @Auto_check.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(exchange_rate(bot))