#q4_sum_series.py
#find sum of series

#define m_series(i) function

def m_series(i):
    
    sum = 0
    for j in range(1,i+1):
        sum+=j/(j+1)
    return(sum)

#printing table

#print headers
print("{0:<4}{1:^6}".format("i","m(i)"))

#print values
for i in range(1,21):
    print("{0:<4}{1:^6.4f}".format(i,m_series(i)))
