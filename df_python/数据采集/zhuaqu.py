# 2021-09-29 13:20:41
# 抓取天气后报
# 网址：
# http://www.tianqihoubao.com/aqi/haerbin.html
import requests
from bs4 import BeautifulSoup

url = "http://www.tianqihoubao.com/aqi/haerbin-202108.html"
vue = requests.get(url)
# 验证

# print(vue.text)


bs = BeautifulSoup(vue.text, "html")

bs = BeautifulSoup(vue.text, "html")
s1 = bs.findAll("tr")
# 遍历trs，输出所有的td
for tds in s1:
    # 遍历tr中的td,这个td里是一个数组，调用数组中的元素
    tr = tds.findAll("td")
    # print(tr[1].text)
    # python a文件处理
    # as 取别名
    with open("tqhb.txt", "a") as f1:
        # f1.write("#")
        str1 = "# "
        for t in range(4):
            str1 = str1 + " " + (tr[t].text.strip())
        str1 = str1 + "\n"
        print(str1)
        f1.write(str1)

    # 文本文件的要求
    # 2021 08-01 优  19   30
    # 2021 08-01 优  19   30
