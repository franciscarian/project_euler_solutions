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