# python that returns the sum of all the numbers in the list.
def sum_numbers(num):
    total = 0
    for num in nums:
        total += num
    return total

nums = [1, 2, 3, 4, 5]
print("The sum is:", sum_numbers(nums))
