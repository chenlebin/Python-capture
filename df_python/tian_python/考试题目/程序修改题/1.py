'''------------------------------------------------------
【程序改错】
---------------------------------------------------------

题目：求如下表达式：

               1       1                     1
      S = 1 + —— + ——— + ...... + ———————
              1+2    1+2+3             1+2+3+......+n

---------------------------------------------------------
注意：不可以增加或删除程序行，也不可以更改程序的结构。
------------------------------------------------------'''


def fun(n):
    s = 0
    # **********FOUND**********
    for i in range(1, n + 1):
        t = 0
        # **********FOUND**********
        for j in range(1, i + 1):
            t = t + j
        # **********FOUND**********
        s += 1.0 / t
    return s


def main():
    n = int(input("请输入一个正整数n："))
    print("S = ", fun(n))


if __name__ == '__main__':
    main()
