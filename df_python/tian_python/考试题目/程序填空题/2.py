'''------------------------------------------------------
【程序填空】
---------------------------------------------------------
题目：编写程序，从键盘输入两个正整数，计算两个数的最大公约数和最小公倍数。
------------------------------------------------------------
注意：除要求填空的位置之外，请勿改动程序中的其他内容。
------------------------------------------------------'''
a = int(input("请输入一个数："))
b = int(input("请输入第二个数："))
if a < b:
    t = a
    a = b
    b = t
p = a * b
# **********SPACE**********
while b != 0:  # todo
    # **********SPACE**********
    r = a % b  # todo
    a = b
    b = r
print("最大公约数", a)
print("最小公倍数", p / a)
