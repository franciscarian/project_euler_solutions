#generate prime
from utilities import Euler_Utilities

def sieve_prime(limit: int) -> list:
    sieve_list = [True for n in range(0, limit)]
    sieve_list[0], sieve_list[1] = False, False
    for number in range(2, limit):
        if sieve_list[number]: #if True
            for prime in range(number*number, limit, number):
                sieve_list[prime] = False
    return sieve_list

def solution():
    p_list = sieve_prime(2000000)
    sum = 0
    for i in range(len(p_list)):
        if p_list[i] is True:
            sum += i
    return sum

import time
start = time.perf_counter()
#print(prime_lists(200000))
print(solution())
end = time.perf_counter()
print(end-start)