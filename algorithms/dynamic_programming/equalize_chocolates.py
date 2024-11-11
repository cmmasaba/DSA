def min_operations(arr):
    # Find the maximum number of chocolates
    max_chocolates = max(arr)
    
    # Initialize dp array
    dp = [float('inf')] * (max_chocolates + 1)

    # Base cases
    dp[0] = 0
    for i in range(1, 5):
        dp[i] = 1

    # Fill dp array
    for i in range(5, max_chocolates + 1):
        dp[i] = 1 + min(dp[i-1], dp[i-2], dp[i-5])

    # Calculate the total operations needed
    total_operations = 0
    for chocolates in arr:
        total_operations += dp[max_chocolates - chocolates]

    return total_operations

# Example usage
arr = [1, 1, 5]
result = min_operations(arr)
print(f"Minimum number of operations: {result}")