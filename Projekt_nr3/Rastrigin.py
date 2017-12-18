"Import matematycznej biblioteki Python"
import math

def get_equation(x, y):
    "Rownanie"
    return 20 + x * x + y * y - 10 * (math.cos(math.pi * 2 * x) + math.cos(math.pi * 2 * y))
