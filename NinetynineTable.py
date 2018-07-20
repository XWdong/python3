# 1、使用range(1,10)  生成 从1 开始到 9的 数列
for i in range(1, 10):
    for j in range(1,i+1):
        # .format() 基本语法是通过 {} 和 : 来代替以前的 %
        # site = {"name": "薛伟东", "age": "25"}
        # print("姓名：{name}, 年龄 {age}".format(**site))
        # 方法一
        # %d 表示以整型十进制格式输出
        # %2d 表示以整数十进制格式输出 实际宽度为  2位
        # print("%d*%d=%2d" % (i, j, i * j), end=" ")
        # 方法二
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()
