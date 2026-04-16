from math import sqrt

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def prime_factors(n: int) -> list:
    if is_prime(n):
        return None       
    else:
        p_factors = []
        for i in range(2, int(sqrt(n))):
            if n % i != 0:
                continue
            elif n % 1 == 0 and not is_prime(i):
                continue
            elif n % i == 0 and is_prime(i):
                p_factors.append(i)
        return p_factors
                
                
#return the prime factors of 210 -> 2,3,5,7
#divide 210 by 2, until its not longer divisible
import time
start_time = time.time()
print(prime_factors(600851475143))
print("--- %s seconds ---" % (time.time() - start_time))