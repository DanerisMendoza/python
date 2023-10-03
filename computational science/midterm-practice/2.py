'''
    A positive integer which is only divisible by 1 and itself is known as prime 
    number.
    For example: 13 is a prime number because it is only divisible by 1 and 13 but, 
    15 is not prime number because it is divisible by 1, 3, 5, and 15.
    Create a program that will accept integer input and check if the number is 
    Prime or not.
'''
import math

def isPrimeNumber(number):
    if(number < 2):
        # automatically number lesss than 2 automatic not primenumber
        # A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers 
        return False
    
    for i in range(2,int(math.sqrt(number)+1)):
        if(number % i == 0):
            return False # The number is divisible by i, so it's not a prime number
        
    return True # If no factors are found, the number is a prime number


input1 = int(input("Enter a Integer: "))
print('prime' if isPrimeNumber(input1) else 'not prime')

'''
    simulation: 4
    2 - 3
    4 / 2 = 2
    ->not prime

    simulation: 6
    2 - 4
        6 / 2 = 3
    ->not prime
    
    simulation: 7
    2 - 3
        7 / 2 = 3.5
    ->prime
'''
