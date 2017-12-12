"""Main Perceptron class """
import random

class Perceptron:
    "Klasa perceptronu"

    def __init__(self, inputs):
        self.inputs = inputs
        self.weights = []
        for i in range(0, inputs):
            self.weights.append(random.uniform(0, 1))

    @staticmethod
    def activation(y_p):
        "funkcja aktywacji"
        if y_p < 0:
            return 0
        return 1

    def sum(self, vector):
        "Sumowanie wag"
        y_p = 0
        for i in range(0, self.inputs):
            y_p += vector[i] + self.weights[i]

        return self.activation(y_p)

    def learn(self, vector, y_value, learning_rate):
        "Uczenie"
        y_p = sum(self, vector)
        for i in range(0, self.inputs):
            self.weights[i] += (y_value - y_p) * learning_rate * vector[i]
