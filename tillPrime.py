def tillPrime(number):
    num = 0
    while num < number:
        num += 1
        if number%num == 0:
            print(num)

tillPrime(15)
