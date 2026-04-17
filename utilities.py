from math import sqrt

class Euler_Utilities:
    def __init__(self):
        pass
    
    def print_message(self, message):
        print(f"This is a test! Message: {message}")
        
    def multiples_sum(self, multiple, limit):
        sum = 0
        i = 0
        while i*multiple < limit:
            sum += i*multiple
            i += 1
        return sum
    
    def fibonacci_generator(self): #using memoization + yield
        #yield holds generator object --> "single iteration point", literally holds at that point
        #yield is to for function to know where to begin. 
        #without these, function would start output with 3
        yield 1
        yield 1 
        previous = 1
        current = 1
        while True:
            previous, current = current, current + previous
            yield current
    
    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def is_palindrome(self, n: int) -> bool:
        return str(n) == str(n)[::-1]
    
    def prime_factors(self, n: int) -> list:
        temp_v = Euler_Utilities()
        if temp_v.is_prime(n):
            return [n]     
        else:
            p_factors = []
            i = 2
            while n%2 == 0:
                n //= 2
                p_factors.append(2)
                
            i = 3
            while i <= sqrt(n):
                while n % i == 0:
                    p_factors.append(i)
                    n//= i 
                i += 2

            if n> 1: #only factors left is 1 (not prime) and a prime number bigger than sqrt(n)
                p_factors.append(n)
            
            return p_factors
    
    def lcm(self, n):
    #find prime factors.
        #iterate through list
        #if not in max_p_factors, add
        #if .count(p_factor) > max_p_factors[p_factor], replace
        #iterate through and multiply.
        max_p_factors = {}
        p_factors = Euler_Utilities()
        for i in range(2, n+1):
            p_factor = p_factors.prime_factors(i)
            for j in p_factor:
                if j not in max_p_factors:
                    max_p_factors[j] = p_factor.count(j)
                else:
                    if p_factor.count(j) > max_p_factors[j]:
                        max_p_factors[j] = p_factor.count(j)
                    continue
        lcm = 1
        for idx in max_p_factors.items():
            curr_mul = idx[0] ** idx[1]
            lcm *= curr_mul
        return lcm
    
    def difference_two_squares(self,a,b):
        return (a+b)*(a-b)
    
    def triangle_number(self, n): 
        return n*(n+1)//2
    
    def iterative_sum_square(self, n): #find sum of the squares up to the number
        sum = 0
        for i in range(1, n+1):
            sum += i**2
        return sum