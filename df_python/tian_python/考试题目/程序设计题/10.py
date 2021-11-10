'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：文本字符分析。 编写程序接收字符串，按照字符出现频率的降序打印字母。

输出实例：

【请输入要分析的字符串，#表示结束：】werwwe
w             3
e             2
r             1
【请输入要分析的字符串，#表示结束：】#
------------------------------------------------------'''
str = input("【请输入要分析的字符串，#表示结束：】")

while str != '#':
    # **********Program**********
    counts = {}
    for ch in str:
        counts[ch] = counts.get(ch, 0) + 1

    items = list(counts.items)
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(items)):
        word, count = items[i]

    # **********  End  **********
    print("{0:<10}{1:>5}".format(word, count))

    str = input("【请输入要分析的字符串，#表示结束：】")
