def main():
    while True:
        try:
            choice = menu()
            if choice == '1':
                choice_one()
            elif choice == '2':
                choice_two()
            elif choice == '3':
                break
            else:
                raise ValueError("Please Enter 1, 2, or 3")
        except ValueError as ve:
            print(ve)


def choice_one():
    while True:
        try:
            sub_choice = submenu()
            if sub_choice == '1':
                while True:
                    try:
                        num = int(input("How far would you like your fibonacci sequence to go? "))
                        fibonacci(num)
                        break
                    except ValueError:
                        print("Please Enter a Positive Number")
            elif sub_choice == '2':
                fib_file = open("fibonacci_description.txt", "r")
                print(fib_file.read())
                break
            elif sub_choice == '3':
                break
            else:
                raise ValueError("Please Enter 1, 2, or 3")
        except ValueError as ve:
            print(ve)


def choice_two():
    while True:
        try:
            sub_choice = submenu()
            if sub_choice == '1':
                while True:
                    try:
                        num = int(input("whats your range for fizzbuzz? "))
                        fizzbuzz(num)
                        break
                    except ValueError :
                        print("Please Enter a Positive Number")
            elif sub_choice == '2':
                fb_file = open("fizzbuzz_description.txt", "r")
                print(fb_file.read())
                break
            elif sub_choice == '3':
                break
            else:
                raise ValueError("Please Enter 1, 2, or 3")
        except ValueError as ve:
            print(ve)


def menu():
    choice = input('What code challenge would you like to see completed and learn more about?\n'
                   '1) Fibonacci\n'
                   '2) Fizzbuzz\n'
                   '3) Exit\n'
                   ': ')

    return choice


def submenu():
    choice = input("Would you like to see it in action or read more about it?\n"
                   "1) All about that action boss!\n"
                   "2) Lemme see them docs!\n"
                   "3) Exit\n"
                   ": ")
    return choice


def fibonacci(num):
    a = 0
    b = 1
    if num <= 0:
        print("Number must be positive")
    elif num == 1:
        return 0
    else:
        sequence = []
        for i in range(num):
            sequence.append(b)
            c = a + b
            a = b
            b = c
        print(sequence)


def fizzbuzz(num):
    for x in range(num + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
            continue
        elif x % 3 == 0:
            print("fizz")
            continue
        elif x % 5 == 0:
            print("buzz")
            continue
        print(x)


main()

