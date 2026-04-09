#this is my solution to the first problem of project euler

#get the sum of all multiples of 3 and 5 under 1000
def multiples_sum(multiple, limit):
    sum = 0
    i = 0
    while i*multiple < limit:
        sum += i*multiple
        i += 1
    return sum

fives = multiples_sum(5, 1000)
threes = multiples_sum(3, 1000)
fifteens = multiples_sum(15, 1000)

print((fives+threes) - fifteens)