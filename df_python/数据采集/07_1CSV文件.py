import requests
from bs4 import BeautifulSoup

url = "http://www.tianqihoubao.com/aqi/haerbin-202108.html"
vue = requests.get(url)
# 验证
# print(vue.text)

bs = BeautifulSoup(vue.text, "html")
trs = bs.findAll("tr")
for tr in trs:
    tds = tr.findAll("td")
    # print(tds[0].text.strip())
    #   CSV  文件格式
    ##  参数1：文件名，文件选项：a 追加
    date = tds[0].text.strip()  ##日期
    zl = tds[1].text.strip()  ##d当日空气质量
    pm = tds[3].text.strip()  ##aqi排名
    pm25 = tds[4].text.strip()  ##PM2.5
    so2 = tds[6].text.strip()  ##So2
    co = tds[8].text.strip()  ##Co
    o3 = tds[9].text.strip()  ##O3
    with open("tqhb02.csv", "a") as f1:
        f1.write(date + "," + zl + "," + pm + "," + pm25 +"," + so2 + "," + co + "," + o3 + "\n")
