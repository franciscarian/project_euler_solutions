#find first triangle number with over 500 divisors
# how to find divisors:
# iterate up until sqrt of number
# check if number/ iteration = whole number
# if yes, then it is a divisor, + divisor + iteration to divisor list
# else continue

# example = 28, 6 divisors
from utilities import Euler_Utilities
from math import sqrt
import time
v = Euler_Utilities()
limit = 500


def unoptimal_solution(limit):
    divisors = []
    tri_num = 1  
    while len(divisors) < limit:
        triangle_number = v.triangle_number(tri_num)
        divisors = []
        for i in range(1, int(sqrt(triangle_number))):
            if (triangle_number%i) == 0:
                if triangle_number//i == i:
                    divisors.append(i)
                    continue
                divisors.append(i)
                divisors.append(triangle_number//i)
        tri_num += 1
    return triangle_number

def optimal_solution(limit):
    tri_num = 1
    divisors = 1
    while divisors < limit:
        triangle_number = v.triangle_number(tri_num)
        triangle_factors = v.prime_factors(triangle_number)
        factors = v.product_prime_factors(triangle_factors)
        divisors = 1
        for idx,key in enumerate(factors):
            divisors *= factors[key]+1
        tri_num +=1
    return triangle_number

start = time.perf_counter()
print(unoptimal_solution(limit)) 
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print(optimal_solution(limit))
end = time.perf_counter()
print(end - start)