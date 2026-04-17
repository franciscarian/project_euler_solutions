#this is my solution to the first problem of project euler

#get the sum of all multiples of 3 and 5 under 1000
from utilities import *

fifth = Euler_Utilities()
#grab solutions for 5
fives = fifth.multiples_sum(5, 1000)

third = Euler_Utilities()
threes = third.multiples_sum(3, 1000)

fifteenth = Euler_Utilities()
#remove solutions that have already been accounted for (multiples of 15)
fifteens = fifteenth.multiples_sum(15, 1000)

print(fives+threes)