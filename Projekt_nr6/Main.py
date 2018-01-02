from math import sqrt
from Kohonen import Kohonen
from Letters import learn_letters
from Letters import test_letters

def learn(kohonens):
    "Funkcja uczenia"
    counter = 0
    winners = []
    for i in range(0, LEARN_SAMPLES):
        winners.append(-1)

    while(unique(winners) != True):
        for i in range(0, LEARN_SAMPLES):
            winner = get_winner(kohonens, learn_letters[i])
            kohonens[winner].learn(learn_letters[i], LEARNING_RATE)

            for j in range(0, NEURONS):
                "Petla uczaca sasiadow"
                if j != winner:
                    if vector_distance(kohonens[winner].weights, kohonens[j].weights) <= NEIGHBOURHOOD_RADIUS:
                        kohonens[j].learn(learn_letters[i], LEARNING_RATE)

        for i in range(0, LEARN_SAMPLES):
            winners[i] = get_winner(kohonens, learn_letters[i])

        counter += 1
        if counter == LIMIT:
            break
    return counter

def unique(winners):
    "Funkcja sprawdza czy siec jest juz nauczona"
    for i in range(0, LEARN_SAMPLES):
        for j in range(i, LEARN_SAMPLES):
            if i != j:
                if winners[i] == winners[j]:
                    return False
    return True

def get_winner(kohonens, vector):
    "Zwraca wygrany neuron"
    winner = 0
    minimum_distance = vector_distance(kohonens[0].weights, vector)
    for i in range(1, NEURONS):
        current_distance = vector_distance(kohonens[i].weights, vector)
        if minimum_distance > current_distance:
            winner = i
            minimum_distance = current_distance

    return winner

def vector_distance(vector1, vector2):
    "Zwraca odleglosc pomiedzy wektorami (miara Manhattan)"
    sum = 0
    for i in range(0, len(vector1)):
        sum += abs(vector1[i] - vector2[i])

    return sqrt(sum)

### Dane wejściowe

LEARNING_RATE = 0.3
INPUTS = 35
NEURONS = 20000
LEARN_SAMPLES = 20
TEST_SAMPLES = 20
LIMIT = 3500
NEIGHBOURHOOD_RADIUS = 6.0

kohonens  = []
for i in range(0, NEURONS):
    kohonens.append(Kohonen(INPUTS))

learn_result =[]
test_result = []
percent = 0
eras = learn(kohonens)

for i in range(0, LEARN_SAMPLES):
    learn_result.append(get_winner(kohonens, learn_letters[i]))
    
for i in range(0, TEST_SAMPLES):
    test_result.append(get_winner(kohonens, test_letters[i]))

for i in range(0, TEST_SAMPLES):
    if learn_result[i] != test_result[i]:
        percent += 1

print("Ilosc epok:", eras)
print("Poprawnosc testowania =", ((percent * 100) / TEST_SAMPLES), "%")
