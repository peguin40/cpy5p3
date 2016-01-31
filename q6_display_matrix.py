#q6_display_matrix.py
#display a n by n matrix using print_matrix(n) function

import random

#define print_matrix(n)

def print_matrix(n):

    for j in range (0,n):
        row = ''
        for i in range(0,n):
            row += str(random.randrange(0,2))
            row += ' '
        print(row)


#get input
integer = int(input("Please enter an integer: "))

#execute print_matrix(n) with integer as n
print_matrix(integer)
