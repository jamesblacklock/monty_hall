from random import randint

def monty_hall(choose):
    doors = [False, False, False]

    car = randint(0, 2)

    doors[car] = True

    choice = randint(0, 2)

    reveal = randint(0, 2)
    while reveal == choice or doors[reveal]:
        reveal = randint(0, 2)

    new_choice = choose(choice, reveal)

    return doors[new_choice]

def switch_choice(choice, revealed):
    new_choice = 0
    while new_choice in (choice, revealed):
        new_choice += 1

    assert new_choice < 3
    return new_choice

def keep_choice(choice, _):
    return choice

def random_choice(choice, revealed):
    new_choice = randint(0, 2)
    while new_choice == revealed:
        new_choice = randint(0, 2)

    assert new_choice < 3
    return new_choice

times = 10_000_000

switch_count = 0
for _ in range(0, times):
    if monty_hall(switch_choice):
        switch_count += 1
print('switch choice:', switch_count/times)

keep_count = 0
for _ in range(0, times):
    if monty_hall(keep_choice):
        keep_count += 1
print('keep choice:  ', keep_count/times)

random_count = 0
for _ in range(0, times):
    if monty_hall(random_choice):
        random_count += 1
print('random choice:', random_count/times)