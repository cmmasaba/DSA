"""An algorithm to find the optimal way of cutting a rod in order to maximize revenue"""

from math import inf

def cut_rod(prices: list, rod_length: int) -> float:
    """Find an the max revenue from cutting a rod of length n in an optimal way.
    Solved using the bottom-up dynamming programming approach.
    
    Args:
        prices: a with prices. Value at key i corresponds to price for rod of length i.
        rod_length: the length of the rod
    Returns:
        the maximum revenue possible
    """
    revenues = [0 for i in range(rod_length+1)]
    sizes = list(range(rod_length))
    for j in range(1, rod_length+1):
        revenue = -inf
        for i in range(1, j+1):
            if revenue < prices[i-1] + revenues[j-i]:
                revenue = prices[i-1] + revenues[j-i]
                sizes[j-1] = i
        revenues[j] = revenue
    return revenues, sizes

def print_cut_rod(prices: list, rod_length: int):
    revenues, sizes = cut_rod(prices, rod_length)
    print(f"The optimal revenue for rod of length {rod_length} is {revenues[rod_length]}")
    print("Rod cut sizes for optimal revenue are:", end=" ")
    while rod_length:
        print(sizes[rod_length-1], end="")
        rod_length = rod_length - sizes[rod_length-1]
        if rod_length:
            print(' -> ', end="")
        else:
            print()

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
rod_length = 4
print_cut_rod(prices, rod_length)