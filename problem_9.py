# a + b + c = 1000
# a < b < c
# asq + bsq = csq

from math import prod, sqrt
import time


def find_pythag_triplet(target):
    for a in range(1,target):
        for b in range(target):
            c = sqrt((a*a) + (b*b))
            if (a+b+c) == target:
                break
        else:
                continue
        break
    return([a,b,c])

start = time.perf_counter()    
print(find_pythag_triplet(1000))    
end = time.perf_counter()
print(end - start)