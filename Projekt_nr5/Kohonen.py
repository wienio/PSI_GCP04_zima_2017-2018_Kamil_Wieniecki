from random import uniform

class Kohonen:

    def __init__(self, inputs):
        "Konstruktor"
        self.inputs = inputs
        self.weights = []
        for i in range(0, inputs):
            self.weights.append(uniform(0, 1))

    def learn(self, vector, learning_rate):
        "Metoda uczenia"
        for i in range(0, self.inputs):
            self.weights[i] += learning_rate * (vector[i] - self.weights[i])
