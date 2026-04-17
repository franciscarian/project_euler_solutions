from utilities import Euler_Utilities

#finding lcm by prime factors.
#finding prime factors of the numbers, 
#multiplying by largest prime factor, 
# e.g. find lcm of 15 and 27
# 15 = 3 x 5
# 27 = 3^3
# lcm = 3^3 x 5 = 135, lcm found.

solution = Euler_Utilities()
print(solution.lcm(20))
