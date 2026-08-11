def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)
    
from utilities import Euler_Utilities
import time

v = Euler_Utilities()

def solution(number):
    sum = 0
    answer = v.factorial(number)
    for i in str(answer):
        sum += int(i)
    return sum

start = time.perf_counter()    
print(solution(100))
end = time.perf_counter()
print(end - start)

