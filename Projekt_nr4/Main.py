from Emoji import emoji
from Emoji import confused_emoji
from Emoji import emoji_type
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

    while unique(winners) == False:
        for i in range(0, NEURONS):
            for j in range(0, EMOJI):
                hebbs[i].learn_without_supervising(emoji[j], LEARNING_RATE, FORGETTING_RATE, HEBB_FORGETTING)

            for j in range(0, EMOJI):
                winners[j] = test_hebb(hebbs, emoji[j])

        counter += 1
        if counter == limit:
            break

    return counter

def unique(winners):
    "Funkcja sprawdza czy elementy w tablicy sa unikalne, pomoc w nauce"
    print(winners)
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

INPUTS = 65
LEARNING_RATE = 0.01
FORGETTING_RATE = LEARNING_RATE / 6.0
NEURONS = 5
EMOJI = 4

HEBBS = []
for i in range(0, NEURONS):
    HEBBS.append(Hebb(INPUTS))

ERAS = learn(HEBBS)

## po nauce

print("Po nauce")
for i in range(0, EMOJI):
    winner = test_hebb(HEBBS, emoji[i])
    print("Wygrany dla emotikony", emoji_type[i], "neuron:", winner)

print("Testowanie")
for i in range(0, EMOJI):
    winner = test_hebb(HEBBS, confused_emoji[i])
    print("Wygrany dla emotikony", emoji_type[i], "neuron:", winner)

print("Ilosc epok =", ERAS)
