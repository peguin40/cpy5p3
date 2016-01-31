#q2_display_pattern.py

#define function display_pattern()

def display_pattern(n):

    #getting the width of the last output
    last_output = ''
    for numbers in range(n+1):
        last_output += ' '                      #append a space for easier readability
        last_output += str(numbers)             #append number to end of string

    width = len(last_output)

    #printing triangle pattern
    for i in range(1,n+1):
        b=' '                                   #initialize b
    #printing single lines in triangle
        for x in range(1,i+1):
            b+=' '                              #append a space for easier readability
            b+=str(x)                           #append number to end of string

        print("{0:>{1}}".format(b,width))

#getting an input
while True:
    try:
        n = int(input("Please enter an integer: "))
        break

    #check for invalid input
    
    except Exception as e:
        print("Invalid input!")
        print("Error: ",e)

#execute function
display_pattern(n)
