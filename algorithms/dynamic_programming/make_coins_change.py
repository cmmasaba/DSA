"""
Objective
---------
Given a target amount n and a list of coin denominations, find all the possible different ways
to make change for the target amount using the the given coin demoninations.

Characterizing the structure of the optimal solution
----------------------------------------------------
For each coin denomination given there exists two choices we can make:
     i) include the coin denomination in the current combination
    ii) exclude the coin denomination from the current denomination
The binary decision is at the heart of how the solution to the problem is approached.
If we go with option 1, we now need to solve a smaller subproblem of making change for the
remaining amount after subtracting the current coin denomination from the target amount.
If we go with option 2, we move on to consider the next coin denomination while keeping our
target amount the same.
By systematically considering both these choices for each coin we can be certain that the
algorithm explores all possible combinations for making change.
Overlapping problems arise since the ways of making change for smaller amounts are calculated
repeatedly.

Recursively defining the value of the optimal solution
------------------------------------------------------
The recurring problem is how to find ways of making change for smaller amounts using a smaller
subset of denominations available.
Let f(n, m) be the function that finds the number of ways to make change for amount n using
the first m coin denominations.
        f(n,m) = f(n, m-1) + f(n-coins[m-1], m)
    f(n, m-1) represents excluding the mth coin
    f(n-coins[m-1], m) represents including the mth coin

    Base cases:
        if n==0, there i 1 way of making change, i.e. using no coins
        if n<m, there is 0 ways of making change
        if m=0(no coins available) and n>0, there is 0 ways of making change
    
    Recursive solution

    MAKE_CHANGE(amount, coins, index):
        if amount == 0
            return 1
        if amount < 0 AND index >= len(coins)
            return 0
        include = f(amount - coins[index], coins, index)
        exclude = f(amount, coins, index+1)

        return include + exclude
    
        This solution is replaced by the bottom up implementation below
"""

def make_change(amount, denominations):
    """Find the different ways there are to make change for amount given.

    Args:
        amount: the coin to find ways of making change for.
        denominations: a list with the available coin denominations.
    Returns:
        the number of ways to make change for the given coin.
    """
    n = len(denominations)
    ways = [[0]*(amount + 1) for _ in range(n + 1)]

    # Base case, there is one way to make change for 0
    for i in range(n + 1):
        ways[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if denominations[i - 1] <= j: # Can we use the current coin denomination to make change for the current amount
                ways[i][j] = ways[i - 1][j] + ways[i][j - denominations[i - 1]]
            else:
                ways[i][j] = ways[i - 1][j]

    return ways[n][amount]