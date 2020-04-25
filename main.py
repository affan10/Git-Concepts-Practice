main_list = [10, 12, 13, 43, 20, 15, 27, 18, 29, 42]

# Simple squaring of all elements of main_list
def list_comprehension_squared(list):
    # For rebasing practice
    # Check if list is not empty
    if list:
        # Quadruple all numbers
        temp_list = [x**4 for x in list]
        func = lambda x: x + 10
        return map(func, temp_list)

print(list(list_comprehension_squared(main_list)))

# Return even numbers only
def list_comprehension_even_numbers(list):
    # For rebasing practice
    # Check if list is not empty
    if list:
        # Floor divide by 3 and then add 15 to all numbers
        temp_list = [ (x//3) + 15 for x in list]
        add_10_func = lambda x: x + 10
        return map(add_10_func, temp_list)
    return "List does not exists!"


print(list(list_comprehension_even_numbers(main_list)))


def yet_another_func(list):
    sorted_list = sorted(list)
    greater_than_25 = lambda x: x > 25
    return filter(greater_than_25, sorted_list)

print(list(yet_another_func(main_list)))
