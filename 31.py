from time import time
"""
5: 
5
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

Link that explains the solution: https://www.youtube.com/watch?v=jaNZ83Q3QGc
"""
start_time = time()
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
# Create an array with target  + 1 amount elements 
possible_combinations  = [1 if n == 0 else 0 for n in range(0, target + 1)]

# For each coin in coins
for coin in coins:
    # Start from coin so that we never get an index that is less than the coin (this avoids having to check if the index is greater than coin).
    for i in range(coin, target + 1):
        # Add the value of the item at the index i - coin and add it to the value of the item at the index i
        # Note: e.g. i - coin could be 50 - 25 --> 25. So: possible_combinations[50] += possible_combinations[25] 
        possible_combinations[i] += possible_combinations [i - coin]

# Find the amount of combinations for target 200
print(possible_combinations[-1])
end_time = time()
print("Time taken: ", end_time - start_time)