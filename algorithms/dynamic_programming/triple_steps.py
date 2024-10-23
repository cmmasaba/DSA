"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""


def steps(num_stairs):
    memo = [-1 for _ in range(num_stairs+1)]
    return count_ways(num_stairs, memo)

def count_ways(num_stairs, memo):
    """Top-down solution with memoization"""
    if num_stairs < 0:
        return 0
    elif  num_stairs == 0:
        return 1
    elif memo[num_stairs] > -1:
        return memo[num_stairs]
    else:
        memo[num_stairs] = count_ways(num_stairs-1, memo) + count_ways(num_stairs-2, memo) + count_ways(num_stairs-3, memo)
        return memo[num_stairs]
