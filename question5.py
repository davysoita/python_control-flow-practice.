# Python function that takes a dictionary as input and prints all the keys whose values are even numbers
def print_even_value_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)
sample_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(sample_dict)
