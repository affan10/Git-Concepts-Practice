import random

main_list = [12, 10, 93, 77, 42, 74, 8, 5, 3]

# Method level comment for randomize
def randomize(list):
    rand_list = random.sample(list, len(list))
    diff_func = lambda a, b: a * b
    print(list)
    print(rand_list)
    diff_list = list(map(diff_func, list, rand_list))
    return diff_list

print(randomize(main_list))
