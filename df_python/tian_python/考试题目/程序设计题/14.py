'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：实现isPrime()函数，输入一个大于1的正整数，判断其是否为素数，是则
      返回True，否则返回False。

运用实例：
【请输入一个大于1的正整数:】5
True
【请输入一个大于1的正整数:】7
True
【请输入一个大于1的正整数:】9
False
【请输入一个大于1的正整数:】6
False
【请输入一个大于1的正整数:】0
------------------------------------------------------'''

# **********Program**********
import math


def isPrime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
        if i == num - 1:
            return True


def isPrime1(num):
    v = num
    n = int(math.sqrt(v) + 1)
    for i in range(2, n):
        if v % i == 0:
            return False
    else:
        return True


# **********  End  **********


def main():
    num = eval(input("【请输入一个大于1的正整数:】"))
    while num != 0:
        print(isPrime(num))
        num = eval(input("【请输入一个大于1的正整数:】"))


if __name__ == '__main__':
    main()
