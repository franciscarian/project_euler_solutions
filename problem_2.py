#problem 2

#find sum of even-numbered fibonacci numbers under 4,000,000

#fibonacci:
#defined as n = n-1 + n-2
#memoization, use a dictionary to store recent numbers, then yes!

from utilities import Euler_Utilies

fib_obj = Euler_Utilies()
fib_gen = fib_obj.fibonacci_generator()

sum = 0      
for idx in fib_gen:
    if idx > 4000000:
        break
    if idx % 2 == 0:
        sum += idx        
    if idx % 2 == 1:
        continue
print(sum)
    

    