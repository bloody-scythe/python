# Checks if a number is prime
def prime(num):
    from math import floor, sqrt
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for div in range(3, floor(sqrt(num)),2):
        if num % div == 0:
            return False
    return True

# Iterates over prime numbers
def prime_iter(start = 1, limit='inf'):
    num = start
    if limit == 'inf':
        while True:
            if prime(num):
                yield num
            num += 1
    else:
        while num <= limit:
            if prime(num):
                yield num
            num += 1
