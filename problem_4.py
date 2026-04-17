#start counting down from 1000, then multiply 1000-a, and 1000-b
#check if int = int[::-1] (is_palindrome())
from utilities import Euler_Utilities

palin = Euler_Utilities()
def solution():
    palindrome = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            num = i*j
            if palin.is_palindrome(num):
                palindrome.append(num)
                break
            else:
                continue
    return max(palindrome)

print(solution())

