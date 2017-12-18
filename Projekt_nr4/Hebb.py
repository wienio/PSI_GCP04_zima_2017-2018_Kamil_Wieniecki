"Import funkcji losujacej Pythona"
from random import uniform
import math

class Hebb:
    """Klasa HEBB"""

    def __init__(self, inputs):
        "Konstruktor"
        self.inputs = inputs
        self.weights = []
        for i in range(0, inputs):
            self.weights.append(uniform(0, 1))

    @staticmethod
    def activation(y_p):
        "Funkcja aktywacji"
        return (1.0 / 1 + math.pow(math.e, - y_p))

    def sum(self, vector):
        "Sumator"
        y_p = 0
        for i in range(0, self.inputs):
            y_p += vector[i] * self.weights[i]

        return y_p

    def learn_without_supervising(self, vector, learning_rate, forgetting_rate, is_forgetting):
        "Nauka bez nauczyciela"
        y_p = self.activation(self.sum(vector))

        for i in range(0, self.inputs):
            if is_forgetting:
                self.weights[i] = (1 - forgetting_rate) * self.weights[i] + learning_rate * vector[i] * y_p
            else:
                self.weights[i] += learning_rate * vector[i] * y_p

    def test(self, vector):
        "Funkcja testujaca i zwracajaca wynik z neuronu"
        return self.activation(self.sum(vector))

    def normalize_weights(self):
        "Funkcja normalizujaca wagi"
        dl = 0
        for i in range(0, self.inputs):
            dl += math.pow(self.weights[i], 2)
        
        dl = math.sqrt(dl)
        for i in range(0, self.inputs):
            if self.weights[i] > 0 and dl != 0:
                self.weights[i] = self.weights[i] / dl
