from Perceptron import Perceptron
from random import randint

x1 = []
x2 = []
era = 5
points_counter = 15
perceptron = Perceptron()

for i in range (era * points_counter):
    first_number = randint(0,1)
    second_number = randint(0,1)

    if first_number == 0:
        first_number -= 1
    if second_number == 0:
        second_number -= 1

    x1.append(first_number)
    x2.append(second_number)

for i in range (1 , era + 1):
    for j in range (points_counter):
        perceptron.train(x1[j*i], x2[j*i])

for i in range (era * points_counter):
    perceptron.display(x1[i],x2[i])
