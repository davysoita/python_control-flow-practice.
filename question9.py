# python  function that accepts a list of integers and a target sum.
def has_pair_with_sum(num, get_sum):
    seen_nums = set()
    for number in num:
        complement = get_sum - number
        if complement in seen_nums:
            return True
        seen_nums.add(number)
    return False
num = [1, 2, 3, 4, 5]
target_sum = 8
print(has_pair_with_sum(num, target_sum))
