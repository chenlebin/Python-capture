'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，
      然后输出到一个磁盘文件"test.txt"（存放到试题文件夹下）中保存。

------------------------------------------------------'''


def main():
    string = input("【please input a string:】")

    # **********Program**********
    xx = list(string)
    xx1 = []
    for i in xx:
        xx1.append(i.upper())
    print(xx1)
    with open('test.txt', 'w+') as file1:
        for i in xx1:
            file1.write(i + "\t")


# **********  End  **********
if __name__ == '__main__':
    main()
