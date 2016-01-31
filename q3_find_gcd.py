#q3_find_gcd.py
#finding gcd of 2 integers

#defining gcd() function with 2 args

def gcd(m,n):
    if m>n:
        gcd = n
        while m%gcd !=0:
            gcd -=1
        return(gcd)
    elif n>m:
        gcd = m
        while n % gcd !=0:
            gcd-=1
        return(gcd)
    else:
        return(m)

#getting inputs

#First Integer
while True:
    try:
        n1 = int(input("Enter First Positive integer: "))
        break
    #Verify Integer
    except Exception as e:
        print("Invalid Input! Error: ",e)

#Second Integer
while True:
    try:
        n2 = int(input("Enter Second integer: "))
        break
    #Verify Integer
    except Exception as e:
        print("Invalid Input! Error: ",e)

#execute gcd() function

print(gcd(n1,n2))
