#-*- coding:utf-8 -*-

#这里是gay里gay气的神经元！
import numpy as np

class Perceptron:

    def __init__(self, weights = np.array([100]), threshold = 0):

        self.weights = weights
        self.threshold = threshold

    def activate(self,inputs):

        strength = np.dot(inputs, self.weights)
        if strength >= self.threshold:
            result = 1
        else:
            result = 0
        return result