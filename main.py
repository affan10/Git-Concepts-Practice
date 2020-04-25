main_list = [10, 12, 13, 20, 15, 27, 18, 29, 42]

def list_comprehension_mult(list):
    return [x**2 for x in list]

print(list_comprehension_mult(main_list))

def list_comprehension_mult_even(list):
    return [x**2 for x in list if x % 2 == 0]

print(list_comprehension_mult_even(main_list))