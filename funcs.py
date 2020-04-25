import random

main_list = [12, 10, 93, 77, 42, 74, 8, 5, 3]

# Function shuffles a list by creating a copy
def randomize(list):
    return random.shuffle(list)

print(randomize(main_list))
