#-*- coding:utf-8 -*-
from Perceptron import *

class Network:


    #新任务：输入三个电平，输出格式为[move,turn_left]的Boolean List
    def __init__(self):
        self.p11=Perceptron(100,50)
        self.p12=Perceptron(100,100)

        self.p21=Perceptron([100,-100],100)

    def run(self,in_sensor):
        p11_result=self.p11.activate(in_sensor)
        p12_result=self.p12.activate(in_sensor)
        p21_result=self.p21.activate([p11_result,p12_result])

        return [p12_result,p21_result]
    
    
#测试神经网络！
aNetwork=Network()
print aNetwork.run(1)
print aNetwork.run(0.5)
print aNetwork.run(0)


