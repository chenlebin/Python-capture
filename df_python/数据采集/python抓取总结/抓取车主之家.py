# user agent：
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
"""
todo                         抓取车主之家的数据
网站：http://dealer.16888.com/?tag=search&pid=31&brandId=57248
我想对全国所有宝马4s店的信息进行收集，包括4s店的店名和联系方式所在地和在售车型数量，浏览器使用的是Chrome。
时间：2021-11-10-10:31

"""

# 导入http请求库requests
import requests
# 导入数据采集库bs4
from bs4 import BeautifulSoup
# 导入csv文件格式库
import csv as csv

# 指定user agent 方便服务器识别客户的 系统 浏览器 浏览器语言 浏览器插件 浏览器版本 CPU类型 渲染引擎等
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
# 以字典形式存储这个User-Agent
headers = {'User-Agent': user_agent}
# 定义一个序列来暂存多行数据
rows = []
# 定义一个序列来暂存单行数据
row = []


'''
用for循环遍历一个序列，利用这个序列来遍历多个网站
这个宝马4s店信息的网站总共有33页数，
分析之后发现网站的格式是page来进行区分，
一个page=1,...,33来区分多少页
'''
for i in range(1, 33):
    # requests.get()方法读取网页
    r = requests.get('https://dealer.16888.com/?tag=search&brandId=57248&page={}'.format(i), headers=headers)

    # 创建一个名为soup的实例
    # 调整编码为utf-8类型
    soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf8')
    # 抓取4s店的 店名,在售车型数量
    companys = soup.find_all('div', class_='title')
    # 抓取4s店的 电话号码
    dianhua = soup.find_all('div', attrs={"camp clearfix"})
    # 中间变量用于抓取4s店的 所在地
    suozaidi = soup.find_all('div', class_='dealer-city')
    # 中间变量用于抓取4s店的 在售车型数量
    # for cx in companys:
    #     cx2=cx.find('em')
    #     print(cx2)

    j = 0
    # todo 抓取数据
    for company in companys:
        # 抓取a标签中的数据
        a = company.find('a')
        cx = company.find('em')
        for s in suozaidi:
            szd = s.find('p')
            # print(aa.text)
            dh = dianhua[j].find('em')
            # print(ppp.text)
            row = [a.string, dh.string, szd.string, int(cx.string)]
        print(row)
        # 方便获取电话号码
        j = j + 2
        # 将单行数据放入到全局序列rows中方便存储到csv文件中
        rows.append(row)
    print(rows)


# todo 将抓取的数据进行写入csv文件方便后续分析
# place定义的是抓取的地区
place = '全国'
header = ['公司-' + place, '电话号', '所在地', '在售车型数量']
# 使用文件操作with open 新建一个文件以追加的模式进行写入数据
# 修改编码格式为中文国标码GBK，文件取别名为f
with open('车主之家4s店数据.csv', 'a+', encoding='gbk') as f:
    # 调用csv库将需要写入的文件 f 作为参数
    f_csv = csv.writer(f)
    # writerow  写入单行数据--题头
    f_csv.writerow(header)
    # writerows 写入多行数据
    f_csv.writerows(rows)
