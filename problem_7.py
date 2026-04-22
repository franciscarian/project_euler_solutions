#use sieve prime generator, 
from utilities import Euler_Utilities

def naive_solution(limit): #to obtain solution
    v = Euler_Utilities()
    primes = []
    i = 2
    while len(primes) < limit:
        if v.is_prime(i):
            primes.append(i)
        i += 1
    return primes[limit-1]

def sieve_prime(limit: int) -> list:
    sieve_list = [True for n in range(0, limit)]
    sieve_list[0], sieve_list[1] = False, False
    for number in range(2, limit):
        if sieve_list[number]: #if True
            for prime in range(number*number, limit, number):
                sieve_list[prime] = False
    primes = [number for number, state in enumerate(sieve_list) if state]
    return primes 
    
def faster_solution():
    primes = sieve_prime(104744)
    return primes

import time
start = time.perf_counter()
print(naive_solution(10001))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(faster_solution())
end = time.perf_counter()
print(end-start)