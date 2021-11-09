# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:58:09 2021

@author: sherin
"""
# solution 3

import math
def listPrimes(n):
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False
    for i in range(int(math.sqrt(n))+1):
        if isPrime[i]:
            for j in range(i*i,len(isPrime),i):
                isPrime[j] = False
    return [i for (i,prime) in enumerate(isPrime) if prime]

            

def sumPrimes(n):
    return sum(listPrimes(n))

#print(listPrimes(20))
print(sumPrimes(1999999))

# import math
# def sum2MPrimes():
#     N = 2000000
#     noprimes = set(j for i in range(2, 8) for j in range(i*2, N, i))
#     primes = [x for x in range(2,N) if x not in noprimes]
#     noprimes = list(noprimes)
#     noprimes.extend([0,1])
#     allnums=noprimes+primes
#     allnums = sorted(allnums)
#     print(max(allnums))
#     print(N-len(allnums))
#     print(primes[:10])
#     print(noprimes[:10])
#     print(allnums[:10])
#     print(sum(primes))
    
    # return sum(primes)
# sum2MPrimes()
# # Solution 2
# primes_below_number = 2000000
# numbers = [v % 2 != 0 for v in range(primes_below_number)]
# numbers[0] = False
# numbers[1] = False
# numbers[2] = True

# number = 3

# while number < primes_below_number:
#     n = number * 3  # We already excluded even numbers
#     while n < primes_below_number:
#         numbers[n] = False
#         n += number
#     number += 1
#     while number < primes_below_number and not numbers[number]:
#         number += 1
# #print(len(numbers))
# sum_of_numbers = sum(map(lambda index_n: index_n[1] and index_n[0] or 0, enumerate(numbers)))

# print(sum_of_numbers)     
# #print(sum2MPrimes())