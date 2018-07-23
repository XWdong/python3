# coding=utf-8
import math
class AreaCompute:
    # def __init__(self,a,b,c):
    #     self.a = a
    #     self.b =b
    #     self.c =c

    # 三角形
    def san(self):
        a = float(input('请输入三角形的底：'))
        b = float(input('请输入三角形的高：'))
        print("三角形的面积是:{:.2f}".format(a * b / 2))
    # 等边三角形
    def equalSan(self):
        a = float(input('请输入等边三角形的边：'))
        print("等边三角形的面积是:{:.2f}".format((math.sqrt(3) *a *a) / 4))
    # 长方形
    def chang(self):
        a = float(input('请输入长方形的宽：'))
        b = float(input('请输入长方形的高：'))
        print("长方形的面积是:{:.2f}".format(a * b))
    # 正方形
    def zheng(self):
        a = float(input('请输入在方形的边长：'))
        print("正方形的面积是:{:.2f}".format(a * a))
    # 圆形
    def yuan(self):
        a = float(input("请输入圆的半径:"))
        print("圆面积约为:{:.2f}".format(math.pi * a * a))
    # 椭圆
    def Ellipse(self):
        a = float(input("请输入长半轴长："))
        b = float(input("请输入短半轴长："))
        area = float(math.pi * a * b)
        print("椭圆面积约为:{:.2f}".format(area))
    # 梯形
    def Trapezoid(self):
        a = float(input("请输入上底边长度："))
        b = float(input("请输入下底边长度："))
        c = float(input("请输入高："))
        TrapezoidArea = float((a + b) * 2 / c)
        print("梯形的面积为：{:.2f}".format(TrapezoidArea))
# flag是true 的时候循环，是false的时候结束循环
# area = AreaCompute(3,3,3)
area = AreaCompute()
flag = True
while flag:
    print( '欢迎来计算面积~~~,请输入你要计算面积的图形：（1.三角形，2.等边三角形,3.圆，4.椭圆，5.梯形，6.长方形，7.正方形，0.退出）')
    tag = input('请输入编号：')
    if tag == '1':
        area.san()
    elif tag == '2':
        area.equalSan()
    elif tag == '3':
        area.yuan()
    elif tag == '4':
        area.Ellipse()
    elif tag == '5':
        area.Trapezoid()
    elif tag == '6':
        area.chang()
    elif tag == '7':
        area.zheng()
    elif tag == '0':
        flag = False
        '\n已经退出'
