# coding=utf-8
import math
class AreaCompute:
    def __init__(self):
        self.PI = math.pi
    # 三角形
    def san(self,a,b):
        print("三角形的面积是:{:.2f}".format(a * b / 2))
    # 等边三角形
    def equalSan(self,a):
        print("等边三角形的面积是:{:.2f}".format((math.sqrt(3) * a * a) / 4))
    # 长方形
    def chang(self,a,b):
        print("长方形的面积是:{:.2f}".format(a * b))
    # 正方形
    def zheng(self,a):
        print("正方形的面积是:{:.2f}".format(a * a))
    # 圆形
    def yuan(self,a):
        print("圆面积约为:{:.2f}".format(self.PI * a * a))
    # 椭圆
    def Ellipse(self,a,b):
        print("椭圆面积约为:{:.2f}".format(self.PI*a *b))
    # 梯形
    def Trapezoid(self,a,b,c):
        print("梯形的面积为：{:.2f}".format((a + b) * 2 / c))
# flag是true 的时候循环，是false的时候结束循环
# area = AreaCompute(3,3,3)
area = AreaCompute()
area.san(5,6)#三角形面积
area.equalSan(6)#等边三角形
area.chang(5,6)#长方形
area.zheng(6)#正方形
area.yuan(6)#圆形
area.Ellipse(5,6)#正方形
area.Trapezoid(5,6,7)#梯形

