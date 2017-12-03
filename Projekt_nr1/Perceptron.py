import random

# bramka logiczna OR

class Perceptron:

    def __init__(self):
        self.learning_speed = 0.02

        self.weight = [0,0,0]
        self.weight[0] = random.uniform(-1,1)
        self.weight[1] = random.uniform(-1,1)
        self.weight[2] = random.uniform(-1,1)

        self.bias = 1

    def display(self, x1, x2):
        if x1 == 1:
            print ("TRUE or", end='')
        else:
            print ("FALSE or", end='')
        if x2 == 1:
            print (" TRUE = ", end='')
        else:
            print (" FALSE = ", end='')
        
        self.guess(x1, x2)
        if self.result == 1:
            print ("TRUE")
        else:
            print ("FALSE")

    def guess(self, x1, x2):
        self.result = x1*self.weight[0] + x2*self.weight[1] + self.bias*self.weight[2]
       
        if self.result >= 0:
            self.result = 1
        else:
            self.result = -1
        return self.result

    def train(self, x1, x2):
        if x1 == -1 and x2 == -1:
            self.desired = -1
        else:
            self.desired = 1

        error = self.desired - self.guess(x1,x2)
        self.weight[0] += self.learning_speed * error * x1
        self.weight[1] += self.learning_speed * error * x2
        self.weight[2] += self.learning_speed * error * self.bias