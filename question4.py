# python that accepts a list of strings and returns a new list where each string is reversed
def my_strings(strings):
    my_list = [s[::-1] for s in strings]
    return my_list
strings = ["apple", "banana", "cherry"]
print(my_strings(strings))
