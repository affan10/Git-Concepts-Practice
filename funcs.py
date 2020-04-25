import random

main_list = [12, 10, 93, 77, 42, 74, 8, 5, 3]

def randomize(list):
    return random.sample(list, len(list))

print(randomize(main_list))
