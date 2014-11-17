# understanding yield function and generators
from math import sqrt

def get_primes(number):
    while True:
        if is_prime(number):
#            number = yield number #before calling funstion again I need to name_of_generator.send(new_number)
            yield number #next time i call this function it tart from last 'returned' argument. I need yo use next(name_of_generator)
        number+=1

def is_prime(number):
    if number>1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number)+1),2):
            if number % current == 0:
                return False
        return True
    return False
