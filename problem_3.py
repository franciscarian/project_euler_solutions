from utilities import Euler_Utilities
                    
#return the prime factors of 210 -> 2,3,5,7
#divide 210 by 2, until its not longer divisible
import time
start_time = time.time()
solution = Euler_Utilities()
print(solution.prime_factors(600851575143))
print("--- %s seconds ---" % (time.time() - start_time))
