#!usr/bin/env python3

grade_book = [100,97, 65,89, 22, 79,86,70,60,50, 93, 84, 71, 65, 14,9,0,1]

def number_of_grades(grades):
    A = 0
    B = 0
    C = 0
    D = 0
    F = 0
    for grade in grades:
        if grade > 90:
            A += 1
        elif grade > 80:
            B += 1
        elif grade > 70:
            C += 1
        elif grade > 60:
            D += 1
        else:
            F += 1

    grade_counter = {"A":A, "B":B, "C":C, "D":D, "F":F}
    print(grade_counter)

number_of_grades(grade_book)
