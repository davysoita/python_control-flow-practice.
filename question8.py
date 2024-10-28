# python a function that takes a dictionary and an integer n as input and returns a list of keys from the dictionary
# where the value is greater than n.
def keys_with_values_greater_than(dictionary, n):
    result = []
    for key, value in dictionary.items():
        if value > n:
            result.append(key)
    return result

sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_with_values_greater_than(sample_dict, n))
