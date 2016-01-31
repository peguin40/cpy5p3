#q5_determine_prime.py
#displays first thousand prime numbers

#define is_prime(n) function

def is_prime(n):
    prime = True            #default is_prime(n) to True
    for i in range(2,n):
        if n % i == 0:
            prime = False   #set is_prime(n) to False
            break
    return(prime)

#display prime numbers

#initialize variables used in loops
i = 2                   #number currently checking
number_of_primes = 0 #number of primes displayed
row = ''                #string printed as a row
#generate table
while number_of_primes < 1000:
    #generates row
    if is_prime(i) == True:
        number_of_primes+=1
        row += str(i)
        row += ' '
        if number_of_primes%10 == 0:
            print(row)
            row = ''
    i+=1
