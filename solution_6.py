from math import sqrt
from utilities import Euler_Utilities
#find the sum of the squares up to a number,
#find the square of the sum up to a number,
#find difference (of two sqaures)


def solution(n):
    temp_var = Euler_Utilities()
    a = temp_var.iterative_sum_square(n)
    b = temp_var.triangle_number(n)
    return temp_var.difference_two_squares(b, sqrt(a))

import time
start_time = time.time()
print(int(solution(10)))
print("--- %s seconds ---" % (time.time() - start_time))