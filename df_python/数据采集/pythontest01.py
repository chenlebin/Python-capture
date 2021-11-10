# ctrl+/自动注释
#print("hello world!\n"*10)
'''
    print("hello world!\n"*10)
    就捏马离谱
'''
#输出
print('23'+'10')
print(23+10)
a=12
print(a)
#选择结构
if(a>0):
    print('a大于0')
    print('没毛病')
else:
    print('a小于0')

#输入
#a=input("请输入内容：")
#print(a)


print('========================分割线===========================')
'''上课练习：属入用户的年龄，判断是哪个年龄段
    0~10      少儿
    11~30     青年
    31~50     中年
    50之后    老年
'''
n=int(input("请输入你的年龄："))
print(n)
if(n>0 and n<=10):
    print("少儿")
elif(n>=11 and n<=30):
    print('青年')
elif(n>=31 and n<=50):
    print('中年')
elif(n>50 and n<100):
    print("老年")
else:
    print('寿比南山')
