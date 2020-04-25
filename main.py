main_list = [10, 12, 13, 20, 15, 27, 18, 29, 42]

# Simple squaring of all elements of main_list
def list_comprehension_squared(list):
    # For rebasing practice
    # Check if list is not empty
    if list:
        # Quadruple all numbers
        return [x**4 for x in list]

print(list_comprehension_squared(main_list))

# Return even numbers only
def list_comprehension_even_numbers(list):
    # For rebasing practice
    # Check if list is not empty
    if list:
        # Floor divide by 2 all odd numbers
        return [x//2 for x in list if x % 2 != 0]
    return "List does not exists!"

print(list_comprehension_even_numbers(main_list))
