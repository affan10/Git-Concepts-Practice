import random

main_list = [12, 10, 93, 77, 42, 74, 8, 5, 3]

def randomize(list):
    rand_list = random.sample(list, len(list))
    return rand_list

print(randomize(main_list))
