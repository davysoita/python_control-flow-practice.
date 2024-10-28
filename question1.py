#python program that prints the numbers from 1 to 50 using a for loop
# if the numbers that are divisible by 3, print "Fizz"
#if the number numbers divisible by 5, print "Buzz".
def myrange():
    for j in range(1, 50):
        if j % 3 == 0 and j % 5 == 0:
            print("FizzBuzz")
        elif j % 3 == 0:
            print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else:
            print(j)

myrange()
