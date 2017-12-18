from Hebb import Hebb

HEBB_FORGETTING = True
HEBB_WITHOUT_FORGETTING = False

def learn(hebbs):
    "Funkcja uczenia"
    counter = 0
    limit = 1000
    winners = []
    for i in range(0, NEURONS):
        winners.append(-1)

    while unique(winners) != False:
        for i in range(0, NEURONS):
            for j in range(0, EMOJI):
                hebbs[i].learn_without_supervising(0, LEARNING_RATE, FORGETTING_RATE, HEBB_FORGETTING) ## TODO

            for j in range(0, EMOJI):
                winners[j] = test_hebb(hebbs, 0) ## TODO

        counter += 1
        if counter == limit:
            break

    return counter

def unique(winners):
    "Funkcja sprawdza czy elementy w tablicy sa unikalne, pomoc w nauce"
    for i in range(0, NEURONS):
        for j in range(0, NEURONS):
            if i != j:
                if winners[i] == winners[j]:
                    return False
    return True

def test_hebb(hebbs, emoji):
    "Funkcja zwraca wartosc zwyciezkiego neuronu dla emotikony"
    max = hebbs[0].test(emoji)
    winner = 0
    for i in range(1, NEURONS):
        test = hebbs[i].test(emoji)
        if test > max:
            max = test
            winner = i

    return winner



## Dane wejsciowe

INPUTS = 60
LEARNING_RATE = 0.01
FORGETTING_RATE = LEARNING_RATE / 6.0
NEURONS = 5
EMOJI = 4

HEBBS = []
for i in range(0, INPUTS):
    HEBBS.append(Hebb(INPUTS))

ERAS = learn(HEBBS)