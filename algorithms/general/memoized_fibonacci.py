"""Algorithm that prints the sum of fibonacci numbers from 0 to n.
It uses memoization to optimize the algorithm and reduce its runtime from O(2^n) to O(n)
"""
from typing import List
from array import array

def allFib(number: int):
    cache = array('b', (0 for i in range(number + 1)))
    for i in range(number + 1):
        print(f"{i:<{5}} : {fib(i, cache):>{10}}")

def fib(number: int, cache: List[int]):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif cache[number] > 0:
        return cache[number]
    cache[number] = fib(number - 1, cache) + fib(number - 2, cache)
    return cache[number]

allFib(10)