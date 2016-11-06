#first X many prime numbers
#we know that the numbers 1 and 2 are primes, find the rest

import math

def firstXPrimes(limit):
    primes = [1,2]
    if limit > 0:
        print (1)
        if limit > 1:
            print (2)
            current = 3
            while len(primes) < limit:
                root = int(math.sqrt(current))
                index = 1
                while True:
                    if (primes[index] > root):
                        primes.append(current)
                        print(current)
                        break
                    if (current % primes[index] == 0):
                        break
                    index += 1
                current += 1

firstXPrimes(int(input("How many primes do you want to find? \n")))
