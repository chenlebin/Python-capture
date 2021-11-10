def Factorial(n):
    # **********SPACE**********
    if n == 1:  # todo
        fn = 1

    else:
        # **********SPACE**********
        fn = Factorial(n - 1) * n  # todo
    return fn


n = int(input("请输入正整型数值n："))
# **********SPACE**********
print("结果为：", Factorial(n))  # todo
