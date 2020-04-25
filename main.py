main_list = [10, 12, 13, 20, 15, 27, 18, 29, 42]

# Simple squaring of all elements of main_list
def list_comprehension_squared(list):
    return [x**2 for x in list]

print(list_comprehension_squared(main_list))

# Return even numbers only
def list_comprehension_even_numbers(list):
    return [x for x in list if x % 2 == 0]

print(list_comprehension_even_numbers(main_list))
