"Import Adaline"
from Adaline import Adaline
"Import liter"
from Letters import getLetter

def learn(adaline, inputs, learning_rate, i, j):
    "Funkcja uczenia"
    vector = getLetter(i, j)
    vector_formatter(vector)
    vector_p = []
    vector_p.append(1) #bias

    if i==0:
        letter_size = -1
    else:
        letter_size = 1

    for i in range(0, inputs - 1):
        adaline[i].learn(vector, letter_size, learning_rate)
        vector_p.append(adaline[i].test(vector))
    
    adaline[inputs - 1].learn(vector_p, letter_size, learning_rate)

def test(adaline, letter_number, inputs):
    "Funkcja testujaca"
    result = []

    for i in range(0, letter_number * 2):
        result.append(0)

    vector_p = []
    vector_p.append(1) #bias
    for i in range(0, inputs - 1):
        vector_p.append(0)

    for i in range(0, 2):
        for j in range(0, letter_number):
            vector = getLetter(i, j)
            vector_formatter(vector)

            for k in range(0, inputs - 1):
                vector_p[k + 1] = adaline[k].test(vector)

            result[i * letter_number + j] = adaline[inputs - 1].test(vector_p)

    return result

def vector_formatter(vector):
    "Zamiana 0 na -1 w wektorze"
    for i in range(0, INPUTS):
        if vector[i] == 0:
            vector[i] = -1

### dane wejsciowe

INPUTS = 7
LETTTER_NUMBER = 10
ERAS = 0
LEARNING_RATE = 0.00001
ADALINES = []
CORRECT = []  # -1 --> duża litera, 1 --> mała litera
RESULT = []  # dane wyjsciowe (wyniki testowania)

for i in range(0, INPUTS):
    ADALINES.append(Adaline(INPUTS))

for i in range(0, LETTTER_NUMBER):
    CORRECT.append(-1)

for i in range(LETTTER_NUMBER, 2 * LETTTER_NUMBER):
    CORRECT.append(1)

for i in range(0, 2 * LETTTER_NUMBER):
    RESULT.append(0)

while RESULT != CORRECT:
    for i in range(0, 2):
        for j in range(0, LETTTER_NUMBER):
            learn(ADALINES, INPUTS, LEARNING_RATE, i, j)

    RESULT = test(ADALINES, LETTTER_NUMBER, INPUTS)
    ERAS += 1

print("Ilość potrzebnych kroków do nauczenia:", ERAS)
