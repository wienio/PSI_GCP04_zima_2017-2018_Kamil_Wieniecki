"Losowanie typu double"
from random import uniform

class Adaline:
    """Adaline"""

    def __init__(self, inputs):
        "Konstruktor"
        self.weights = []
        self.inputs = inputs
        for i in range(0, inputs):
            self.weights.append(uniform(0, 1))

    @staticmethod
    def activation(y_p):
        "Funkcja aktywacji"
        if y_p <= 0:
            return -1
        return 1

    def sum(self, vector):
        "Sumowanie"
        y_p = 0
        for i in range(0, self.inputs):
            y_p += vector[i] * self.weights[i]

        return y_p

    def learn(self, vector, y_value, learning_rate):
        "Metoda uczenia"
        y_p = self.sum(vector)

        for i in range(0, self.inputs):
            self.weights[i] += (y_value - y_p) * learning_rate * vector[i]

    def test(self, vector):
        "Metoda testująca"
        return self.activation(self.sum(vector))
