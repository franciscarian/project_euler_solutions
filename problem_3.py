from math import sqrt
from utilities import Euler_Utilies
    
def prime_factors(n: int) -> list:
    prime = Euler_Utilies()
    if prime.is_prime(n):
        return None       
    else:
        p_factors = []
        original_n = n
        for i in range(2, int(sqrt(original_n))):
            if n == 1:
                break
            elif n % i != 0:
                continue
            elif n % 1 == 0 and not prime.is_prime(i):
                continue
            elif n % i == 0 and prime.is_prime(i):
                p_factors.append(i)
                n //= i
        return p_factors
                
                
#return the prime factors of 210 -> 2,3,5,7
#divide 210 by 2, until its not longer divisible
import time
start_time = time.time()
print(prime_factors(600851575143))
print("--- %s seconds ---" % (time.time() - start_time))
