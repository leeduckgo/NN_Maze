#-*- coding:utf-8 -*-
from Perceptron import *

class Network:

    def __init__(self):
        self.p1=Perceptron(100,100)
    def run(self,in_sensor):
        out_sensor=self.p1.activate(in_sensor)
        return out_sensor

#测试神经网络！
aNetwork=Network()
print aNetwork.run(100)
print aNetwork.run(0)
'''

    #新任务：输入三个电平，输出格式为[move,turn_left,turn_right]的Boolean List
    def __init__(self):
        self.p11=Perceptron(100,50)
        self.p12=Perceptron(100,100)
        self.p21=Perceptron([50,50],100)
        self.p22=Perceptron([100,-100],100)

    def run(self,in_sensor):
        p11_result=self.p11.activate(in_sensor)
        p12_result=self.p12.activate(in_sensor)
        p21_result=self.p21.activate([p11_result,p12_result])
        p22_result=self.p22.activate([p11_result,p12_result])
        return [p21_result,p22_result]
'''

