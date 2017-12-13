from Perceptron import Perceptron
from Letters import getLetter

### funkcje

def learn(perceptrons, inputs, learning_rate, i, j):
    vector = getLetter(i, j)
    vector_p = []
    vector_p.append(1)   # bias

    for k in range(0, inputs-1):
        perceptrons[k].learn(vector, i, learning_rate)
        vector_p.append(perceptrons[k].sum(vector))
        
    perceptrons[inputs-1].learn(vector_p, i, learning_rate)

def test(perceptrons, letter_number, inputs):
    results = []
    for i in range(0, letter_number * 2):
        results.append(0)
    vector = []
    vector_p = []
    vector_p.append(1)   # bias
    for i in range(0, inputs-1):
        vector_p.append(0)

    for i in range(0, 2):
        for j in range(0, letter_number):
            vector = getLetter(i, j)
            for k in range(0, inputs-1):
                vector_p[k+1] = perceptrons[k].sum(vector)
            results[i * letter_number + j] = perceptrons[inputs - 1].sum(vector_p)

    return results

 ### funkcje

ERAS = 0
INPUTS = 7
LETTER_NUMBER = 10
LEARNING_RATE = 0.00001

PERCEPTRONS = []
Y = []
RESULT = []

## wypelnienie danymi

for i in range(0, INPUTS):
    PERCEPTRONS.append(Perceptron(INPUTS))

for i in range(0, LETTER_NUMBER):
    Y.append(0)

for i in range(LETTER_NUMBER, LETTER_NUMBER*2):
    Y.append(1)

for i in range(0, LETTER_NUMBER*2):
    RESULT.append(0)

## Uczenie

while Y != RESULT:
    # i = 0 -> duze litery, 1 -> male litery
    for i in range(0, 2):
        for j in range(0, LETTER_NUMBER):
            learn(PERCEPTRONS, INPUTS, LEARNING_RATE, i, j)

    RESULT = test(PERCEPTRONS, LETTER_NUMBER, INPUTS)
    ERAS += 1
    
print("Ilosc krokow do nauki:", ERAS)
    