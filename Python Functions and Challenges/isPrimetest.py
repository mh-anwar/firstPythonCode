def isPrime(number):
    counter1=2
    sum=0
    # if(number == 1 or number == 2)
    if(number==1):
        return True
    if(number==2):
        return True
    while counter1<number:
        if(number % counter1 == 0) :
            return False
        counter1=counter1+1
        if (counter1 == number):
            return True
#END OF FUNCTION

#Start of script
number=10
counter=0
sum=0
while counter<number:
    counter+=1
    if (isPrime(counter)):
        sum+=counter
print (sum)



