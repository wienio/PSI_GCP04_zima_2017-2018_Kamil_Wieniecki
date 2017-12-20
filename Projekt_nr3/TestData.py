from random import uniform
from Rastrigin import get_equation

random_input = []
random_output = []
test_input = []
test_output = []

def my_range(start, end, step):
    "Funkcja do manipulacji kroku dla petli for"
    while start <= end:
        yield start
        start += step

def fill_random_test_input(num):
    "Wypełnienie losowymi wartościami"
    for i in range(0, num):
        first = uniform(-2, 2)
        second = uniform(-2, 2)
        random_input.append([first, second])
        random_output.append(get_equation(first, second))

def fill_test_input(num):
    "Wypelnienie testowych wartosci"
    for i in my_range(-2, 2, num):
        for j in my_range(-2, 2, num):
            test_input.append([i, j])
            test_output.append(get_equation(i, j))
