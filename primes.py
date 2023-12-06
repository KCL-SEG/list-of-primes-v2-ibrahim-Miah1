"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def primes(number_of_primes):
    
    if number_of_primes <= 0:
        raise ValueError("The number must be greater than 0")
    
    
    list = []
    current_number = 2

    while len(list) < number_of_primes:
        if is_prime(current_number):
            list.append(current_number)
        current_number += 1

    return list
