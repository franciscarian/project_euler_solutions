class Euler_Utilies:
    def __init__(self):
        pass
    
    def print_message(self, message):
        print(f"This is a test! Message: {message}")
        
    def multiples_sum(self, multiple, limit):
        sum = 0
        i = 0
        while i*multiple < limit:
            sum += i*multiple
            i += 1
        return sum
    
    def fibonacci_generator(self): #using memoization + yield
        #yield holds generator object --> "single iteration point", literally holds at that point
        #yield is to for function to know where to begin. 
        #without these, function would start output with 3
        yield 1
        yield 1 
        previous = 1
        current = 1
        while True:
            previous, current = current, current + previous
            yield current
 