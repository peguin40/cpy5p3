#q7_convert_ms.py
#converts ms to hours,minutes and seconds as string hours:minutes:seconds

#define convert_ms(n) function

def convert_ms(n):
    #get number of hours
    hours = int(n//(3600000))
    n = n-hours*(3600000)#remove hours from n

    #get number of minutes
    minutes = int(n//60000)
    n = n-minutes*60000#remove minutes from n

    #get number of seconds
    seconds = int(n//1000)

    #display result in format hours:minutes:seconds
    print("{0}:{1}:{2}".format(hours,minutes,seconds))


#get input for milliseconds
while True:
    try:
        milliseconds = int(input("Milliseconds(ms): "))
        break
    except Exception as e:
        print("Invalid Input! Error: ",e)

# execute convert_ms(n) with milliseconds as n

convert_ms(milliseconds)

    
