'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：计算前n个自然数的阶乘之和1!+2!+3!+...+n!的值

---------------------------------------------------------
注意：部分源程序给出如下。请勿改动主函数main和其它函数中的
      任何内容，仅在函数的注释标志之间填入所编写的若干语句。
------------------------------------------------------'''


def main():
    n = int(input("【请输入一个正整数n: 】"))
    result, sum = 1, 1
    # **********Program**********
    for i in range(2, n + 1):
        for j in range(2, i + 1):

            sum *= j
        result += sum
        sum = 1
    # **********  End  **********
    print('%d' % result)


if __name__ == '__main__':
    main()
