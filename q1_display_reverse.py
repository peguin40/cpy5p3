#q1_display_reverse.py
#reverses integer inputted

#input variables
while True:
    try:
        integer = input("Please input an integer: ")
        break
    except Exception as e:
        print("Invalid input!")
        print("Error: ", e)

#reverse integer
        
integer = integer[::-1]

#displat integer

print(integer)
