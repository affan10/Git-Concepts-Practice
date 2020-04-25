import random

main_list = [12, 10, 93, 77, 42, 74, 8, 5, 3]

def randomize(list):
    rand_list = random.sample(list, len(list))
    diff_func = lambda a, b: a - b
    print(list)
    print(rand_list)
    return map(diff_func, list, rand_list)

print(list(randomize(main_list)))
