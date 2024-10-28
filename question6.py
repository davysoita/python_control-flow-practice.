# Python function using a loop that returns the largest number in the tuple.
def find_largest_number(numbers):
    my_largest = numbers[0]
    for number in numbers:
        if number > my_largest:
            largest = number
    return my_largest

numbers = (10, 20, 30, 40, 50)
print(find_largest_number(numbers))  # Output: 50
