'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：重复元素判定。编写一个函数，接受列表作为参数，如果一个元素在列表中出现
      了不止一次，则打印True，否则打印False， 但不要改变原来列表的值。

------------------------------------------------------'''


# **********Program**********
def testReEle(lis):
    if len(set(lis)) == len(lis):
        print("False")
    else:
        print("TRUE")


# **********  End  **********


def get_List():
    lis = []
    ch = input("请输入判定元素，回车表示结束：")
    while ch != '':
        lis.append(ch)
        ch = input("请输入判定元素，回车表示结束：")
    testReEle(lis)


get_List()
