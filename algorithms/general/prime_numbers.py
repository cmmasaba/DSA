from math import sqrt

def isPrime(num: int) -> bool:
    """Check if a number is prime.
    Runtime: O(sqrt(n))

    Args:
        num: the number to check for primeness
    Return:
        True or False
    """
    # check for divisibility on numbers less than or equal to the square root of num
    for x in range(2, sqrt(num)+1):
        if num % x == 0:
            return False
    return True