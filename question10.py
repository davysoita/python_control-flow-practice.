# python function that takes a list of tuples as input
# each tuple contains two elements: a string and an integer
def tuples_to_dict(my_tuples_list):
    result_dict = {}
    for item in my_tuples_list:
        key, value = item
        result_dict[key] = value
    return result_dict

my_tuples_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
print(tuples_to_dict(my_tuples_list))
