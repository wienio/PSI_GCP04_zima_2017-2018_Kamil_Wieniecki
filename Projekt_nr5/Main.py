from Kohonen import Kohonen
from math import sqrt
from Data import flower_to_learn
from Data import florwer_to_test

def learn(kohonens):
    "Funkcja uczenia"
    eras = 0
    winners = []

    for i in range(0, FLOWERS):
        winners.append([])
        for j in range(0, LEARN_SAMPLES):
            winners[i].append(-1)

    while unique(winners) != True:
        for i in range(0, FLOWERS):
            for j in range(0, LEARN_SAMPLES):
                winner = get_winner(kohonens, flower_to_learn[i][j])
                kohonens[winner].learn(flower_to_learn[i][j], LEARNING_RATE)

        for i in range(0, FLOWERS):
            for j in range(0, LEARN_SAMPLES):
                winners[i][j] = get_winner(kohonens, flower_to_learn[i][j])

        eras += 1
        if eras == LIMIT:
            break

    return eras

def unique(winners):
    "Funkcja sprawdza czy siec juz sie nauczyla rozpoznawac kwiaty"

    "Petla sprawdza czy kazdy typ ma jednego zwyciezce"
    for i in range(0, FLOWERS):
        for j in range(1, LEARN_SAMPLES):
            if winners[i][0] != winners[i][j]:
                return False

    "Petla sprawdzajaca wszystkie gatunki, czy jest rozny od zwyciezcow pozostalych gatunkow"
    for i in range(0, FLOWERS):
        for j in range(0, FLOWERS):
            if i != j:
                if winners[i][0] == winners[j][0]:
                    return False
    return True

def get_winner(kohonens, vector):
    "Zwraca wygranego"
    winner = 0
    minimum_distance = vector_distance(kohonens[0].weights, vector)

    for i in range(1, NEURONS):
        current_distance = vector_distance(kohonens[i].weights, vector)
        if  current_distance < minimum_distance:
            winner = i
            minimum_distance = current_distance

    return winner

def vector_distance(vector, vector2):
    "Zwraca odleglosc pomiedzy dwoma wektorami (Manhattan distance)"
    sum = 0
    for i in range(0, len(vector)):
        sum += abs(vector[i] - vector2[i])
    return sqrt(sum)

### Dane wejściowe

LEARNING_RATE = 0.01
INPUTS = 4
NEURONS = 220
FLOWERS = 3
LEARN_SAMPLES = 20
TEST_SAMPLES = 8
LIMIT = 10000

success = 0
fail = 0

while success != 10 and fail != 100:
    kohonens = []
    for i in range(0, NEURONS):
        kohonens.append(Kohonen(INPUTS))

    eras = learn(kohonens)

    if eras != LIMIT:
        success += 1

        print("Po nauce:\n")
        for i in range(0, FLOWERS):
            winner = get_winner(kohonens, flower_to_learn[i][0])
            print("Kwiat [", i, "] wygral =", winner)

        print("\nPo testowaniu:")
        for i in range(0, FLOWERS):
            print("\n")
            for j in range(0, TEST_SAMPLES):
                winner = get_winner(kohonens, florwer_to_test[i][j])
                print("Kwiat [", i, "][", j, "]", "winner =", winner)

        print("Ilosc epok:", eras)
    else:
        fail += 1

print("Ilosc niepowodzen w nauce:", fail)
    