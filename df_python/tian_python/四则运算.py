import os
import random


class SuiJiShu(object):
    '''
    类名：SuiJiShu
    功能：产生2个随机数
    参数：start 开始位置， end 结束位置
    属性：num1, num2 分别是2个随机整数
    方法：__init__
    '''

    def __init__(self, start, end):
        self.num1 = random.randint(start, end)
        self.num2 = random.randint(start, end)


class SiZe(object):
    '''
    类名：SiZe
    功能：出一道题
    方法：
    '''

    def __init__(self, op):
        self.op = op

    def zhengque(self):
        print('√' * 10, '回答正确', '√' * 10)
        return 1;

    def cuowu(self):
        print('x' * 10, '回答错误', 'x' * 10)
        return 0;

    def chuti(self):
        '''
        功能：出一道题目
        输入：op （+ - * /）
        输出：biaodashi 例如5+3
        '''
        self.biaodashi = ''
        while (True):
            suiji = SuiJiShu(1, 10)
            x = suiji.num1
            y = suiji.num2
            if self.op == '/':
                if x % y == 0:  # 能整除
                    break
            elif self.op == '-':
                if x < y:
                    x, y = y, x
                    break
            else:
                break
        self.biaodashi = '{}{}{}'.format(x, self.op, y)  # 构造表达式

    def panduan(self):
        '''
        功能：对所给的表达式进行判断

        输出：无
        '''
        try:
            z = int(input(self.biaodashi + '='))
            if z == eval(self.biaodashi):
                pd = self.zhengque()
                return pd;
            else:
                pd = self.cuowu()
                self.cuotiben()
                return pd;
        except Exception as e:
            print(e)

    def cuotiben(self):
        try:
            with open('cuoti.txt', 'a+') as ctb:
                ctb.write(self.biaodashi + '\n')
        except Exception as e:
            print(e)

    def get_cuoti(self):
        try:
            with open('cuoti.txt', 'r+') as ct:
                global r
                r = ct.readlines()
                if len(r) == 0:
                    print('没有错题')
                else:
                    print("以下是你所有的错题集")
                    print(r)
                    tihao = SuiJiShu(0, len(r)).num1
                    self.biaodashi = r[tihao]
                    global pd
                    pd = self.panduan()
                    if pd == 1:
                        r = r[0:tihao] + r[(tihao + 1):(len(r) + 1)]
                        # print(r)
                        ct.close()
                        os.remove('cuoti.txt')  # 删除文件
                        with open('cuoti.txt', 'w+') as xg:
                            print("恭喜你解决了一道错题，你还剩下的错题是：")
                            for i in r:
                                print(i)
                                xg.write(i)
                            xg.read()
        except Exception as e:
            print('打开错题本错误', e)


def main():
    while (True):
        print('请选择题目类型：')
        print('''
        0、加法题
        1、减法题
        2、乘法题
        3、除法题
        4、错题本
        5、退出''')
        choice = input('请输入您的选择：')
        ops = ['+', '-', '*', '/']

        try:

            if int(choice) < 4:
                op = ops[int(choice)]
                timu = SiZe(op)
                timu.chuti()
                timu.panduan()
            elif choice == '4':
                timu.get_cuoti()

            elif choice == '5':
                exit()
            else:
                print('您的输入有误，请重新输入')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
