from Perceptron import Perceptron

eras = 0
inputs = 7
letter_number = 10
learning_rage = 0.1

perceptrons = []
y = []
result = []

for i in range(0, inputs):
    perceptrons.append(Perceptron(inputs))

print (perceptrons[0].weights[0])

for i in range(0, letter_number):
    y.append(0)

for i in range(letter_number, letter_number*2):
    y.append(1)

for i in range(0, letter_number*2):
    result.append(0)

while 1:
    for i in range(0, 2):
        for j in range(0, letter_number):
            learn()


    @staticmethod
    def learn():
        return 1