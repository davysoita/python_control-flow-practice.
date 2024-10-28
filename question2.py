# Using a while loop, write a function that continuously asks the user for input until they type the word "exit".
# The program should print each word entered by the user before asking for the next input.
def get_input():
    while True:
        user_input = input("Enter a word (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        print(f"You entered: {user_input}")

get_input()
