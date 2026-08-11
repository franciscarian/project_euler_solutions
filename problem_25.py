from utilities import Euler_Utilities

v = Euler_Utilities()


def solution(limit):
    count = 0 
    for idx in v.fibonacci_generator():
        count += 1
        if len(str(idx)) == limit:
            return count
    
print(solution(1000))