#   Zwracajcy 0, 1, 0, 1, ...
def zero_one_infinite():
    while(True):
        yield 0
        yield 1

zero_one_iter = zero_one_infinite()
print("+---+ Zero one iterator +---+")
for i in range(10):
    print(next(zero_one_iter),end=', ' if i != 9 else '\n')

#   Zwracajcy przypadkowo jedna wartosc z N E S W
import random

def random_direction():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)

direction_iter = random_direction()
print("\n+---+ Random direction iterator +---+")
for i in range(13):
    print(next(direction_iter), end=', ' if i != 12 else '\n')

# Zwracajacy numery dni tygodnia
def days_of_week():
    num_days = 7
    while True:
        for day in range(num_days):
            yield day

days_iter = days_of_week()
print("\n+-------+ Week days number iterator +-------+")
for i in range(15):
    print(next(days_iter), end=', ' if i != 14 else '\n')