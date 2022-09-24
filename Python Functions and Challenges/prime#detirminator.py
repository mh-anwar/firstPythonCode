def isPrime(number):
    counter=2
    while counter<number:
        if (number % counter == 0):
            print ("Number is not prime")
            return false
        counter=counter+1
        if (counter == number):
            print ("Number is prime!")
            return true

number = 100
counter=1
sum=2
while counter<number:
       counter= counter + 1

       sum+=counter
    
