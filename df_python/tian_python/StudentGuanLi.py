print(' ' * 20, '欢迎使用员工管理系统', ' ' * 20)
emps = ['孙悟空\t18\t男\t花果山', '猪八戒\t28\t男\t高老庄']
print(emps)
while True:
    print('请选择需要进行的操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.修改员工')
    print('\t5.退出系统')
    user_choice = input('请选择[1-5]:')
    if user_choice == '1':
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n = 1  # 创建一个变量，来表示员工的序号
        # 显示员工信息
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choice == '2':
        emp_name = input('请输入员工的姓名：')
        emp_age = input('请输入员工的年龄：')
        emp_gender = input('请输入员工的性别：')
        emp_address = input('请输入员工的住址：')
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        # 显示一个提示信息
        print('以下员工将被添加到系统中：')
        print('-' * 62)
        print('姓名\t年龄\t性别\t地址')
        print(emp)
        print('-' * 62)
        user_confirm = input('是否确认该操作【Y/N】：')
        if user_confirm.lower() == 'y' or user_confirm.lower() == 'yes':
            emps.append(emp)  # 将员工信息添加到列表中
            print('添加成功！')
        else:
            print('添加已经取消！')
    elif user_choice == '3':
        # 删除操作
        # 根据员工的序号删除
        del_num = int(input('请输入要删除的员工序号：'))
        if 0 < del_num <= len(emps):
            # 输入的序号是合法的
            del_i = del_num - 1
            print('以下员工将被删除：')
            print('-' * 62)
            print('\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{del_num}\t{emp[del_i]}')
            print('-' * 62)
            user_confirm = input('删除员工操作不可恢复，是否确认[Y/N]:')
            if user_confirm.lower() == 'y' or user_confirm.lower() == 'yes':
                emps.pop(del_i)  # pop是列表元素的删除操作
                print('删除成功！')
            else:
                print('删除操作已经取消！')
        else:
            print('用户的序号错误，请重新选择删除员工操作')
    elif user_choice == '4':
        up_num = int(input('请输入要修改的员工序号：'))
        if 0 < up_num <= len(emps):
            # 输入的序号是合法的
            up_i = up_num - 1
            print('以下员工将被修改：')
            print('-' * 62)
            print('\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{up_num}\t{emps[up_i]}')
            print('-' * 62)
            age_num = int(input('请输入修改之后的年龄：'))
            # 将emp序列中的的元素按照制表符  \t  进行切分
            str1=emps[up_i].split("\t")
            # 对切分的数据和需要修改的年龄进行拼接,并将age_num转化为str类型
            ss = str1[0] + "\t" + str(age_num) + "\t" + str1[2] + "\t" + str1[3]
            # 将拼接好之后的数据进行赋值给指定序号的emp
            emps[up_i] = ss
            print("修改之后的员工信息为")
            print('\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{up_num}\t{emps[up_i]}')
    elif user_choice == '5':
        print('欢迎使用本系统，再见！')
        input('点击回车键退出系统')
        break
    else:
        print('您的输入有误，请重新选择！')
    print('-' * 62)
