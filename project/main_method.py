def main():
    """this program is a program to show some basic fundamentals of python while also showing my classmates some common
     interview questions and problem solving exercises"""

    while True:  # the while loop allows for exception handling with the try except statement
        try:
            choice = menu()
            # the if statement allows the use of the menu() function to pick which choice function to call
            if choice == '1':
                challenge(0)
            elif choice == '2':
                challenge(1)
            elif choice == '3':  # will break out of the loop if chosen to exit
                print("Thank you, Hope you learned something!")
                break
            else:  # exception handling to make sure that a menu option is selected and if not loops back to try again
                raise ValueError("Please Enter 1, 2, or 3")
        except ValueError as ve:
            print(ve)


def challenge(num):
    files = ["fibonacci_description.txt", "fizzbuzz_description.txt"]
    chal = ["Fibonacci", "FizzBuzz"]
    # Used to allow a user to learn more about Fibonacci should be changed to allow any choice
    while True:  # allows for continuation of the program and exception handling
        try:
            sub_choice = submenu()
            if sub_choice == '1':
                while True:  # allows for exception handling
                    try:
                        iterations = int(input(f"How far would you like your {chal[num]} sequence to go? "))
                        if chal[num] == "Fibonacci":
                            fibonacci(iterations)
                        elif chal[num] == "FizzBuzz":
                            fizzbuzz(iterations)
                        break
                    except ValueError:
                        print("Please Enter a Positive Number")
                break
            elif sub_choice == '2':  # choice in submenu to learn about fibonacci
                txt_file = open(files[num], "r")
                print(txt_file.read())
                break
            elif sub_choice == '3':
                break
            else:
                raise ValueError("Please Enter 1, 2, or 3")

        except ValueError as ve:
            print(ve)


def menu():
    # used to give the user options of what to see completed or learn about
    choice = input('===============================================================================\n'
                   '| What code challenge would you like to see completed and learn more about?   |\n'
                   '| 1) Fibonacci                                                                |\n'
                   '| 2) Fizzbuzz                                                                 |\n'
                   '| 3) Exit                                                                     |\n'
                   '===============================================================================\n')
    return choice


def submenu():
    # once selected allows user to pick what the want to do
    choice = input("====================================================================\n"
                   "| Would you like to see it in action or read more about it?        |\n"
                   "| 1) All about them visuals boss, Hows it work?!                   |\n"
                   "| 2) Hmmm, Lemme read about it first!                              |\n"
                   "| 3) Back                                                          |\n"
                   "====================================================================\n")
    return choice


def fibonacci(num):
    a = 0
    b = 1
    # taking care of special cases
    if num <= 0:
        print("Number must be positive")
    elif num == 1:
        return 0
    else:
        sequence = []  # storing each iteration in a list to print later
        for i in range(num):
            # appending variable b to sequence as it will be the variable that will give the correct fibonacci number
            sequence.append(b)
            c = a + b
            a = b
            b = c
        # Print the sequence of all numbers after the for loop finishes
        print(sequence)


def fizzbuzz(num):
    # added one to make sure it iterates all the way through and to avoid off by one error
    for x in range(num + 1):
        # makes sure its divisible by 3 and 5
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
            continue
        # makes sure its divisible by 3
        elif x % 3 == 0:
            print("fizz")
            continue
        # makes sure its divisible by 5
        elif x % 5 == 0:
            print("buzz")
            continue
        # prints the number if none of the above are true
        print(x)


# Calling the main method to run the program
main()

