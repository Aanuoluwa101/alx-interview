#!/usr/bin/python3
"""In a text file, there is a single character H.
  Your text editor can execute only two operations in this file: Copy All and Paste.
  Given a number n, write a method that calculates the fewest number of operations
  needed to result in exactly n H characters in the file"""


def minOperations(n):
    """calculates the fewest number of operations
       needed to result in exactly n H characters in the file"""
    if type(n) != int or n < 2:
        return 0

    divisor = 2
    factors = []
    temp_n = n

    while temp_n > 1:
        while temp_n % divisor == 0:
            temp_n//=divisor
            factors.append(divisor)
        divisor+=1

    highest_prime_factor = max(factors)
    if highest_prime_factor == n:
        return highest_prime_factor
    return highest_prime_factor + 1 + ((n // highest_prime_factor) - 1)
