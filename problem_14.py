# collatz is:
# n%2 = 0, n/2
# n%2 = 1, 3n+1
import time
collatz_sequence = []

def naive_collatz(number: int, sque: list) -> None: #reversed sequence
    sque.append(number)
    if number%2 == 1:
        if number == 1:
            return None
        number = int((3*number) + 1)
        naive_collatz(number, sque)
    else:
        number = int(number/2)
        naive_collatz(number, sque)
        
def optimised_collatz(number):
    yield number
    while True:
        if number%2 == 1:
            if number == 1:
                yield 1
            number = (3*number) + 1    
            yield number
        else:
            number = int(number/2)
            yield number

start = time.perf_counter()
naive_collatz(6, collatz_sequence)
print(collatz_sequence)
end = time.perf_counter()
print(end - start)

# start = time.perf_counter()
# for idx in optimised_collatz(6):
#         if idx == 1:
#             print(f'num = {idx}')
#             break
#         print(f'num = {idx}')
# end = time.perf_counter()
# print(end - start)

start = time.perf_counter()
max_len = (1, 1) #starting num, len
curr_max_len = 0
for i in range(1, 1000000):
    curr_max_len = 0    
    for idx in optimised_collatz(i):
        if idx == 1:
            # print(f'num = {idx}')
            curr_max_len += 1  
            break
        # print(f'num = {idx}')
        curr_max_len += 1 
    if curr_max_len > max_len[1]:
        max_len = (i, curr_max_len)        
print(max_len)
end = time.perf_counter()
print(end - start)

# curr_max_len = 0
# for idx in optimised_collatz(327):
#         if idx == 1:
#             # print(f'num = {idx}')
#             curr_max_len += 1  
#             break
#         # print(f'num = {idx}')
#         curr_max_len += 1 
        
# print(327, curr_max_len)

