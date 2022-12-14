from time import time

sum_diagonals = 0
gap_count = 0
gap = 2
n = 1
start_time = time()

""" We are stepping 'gap' amount each time, so we will always only get the numbers on the diagonal (This is illustrated and explained on the document attached)."""
# While n isn't the last number (e.g. in a 9x9 tile, the last number would be 81)
while n <= (1001 * 1001):

    # Add the value of n to the sum of diagonals
    sum_diagonals += n
    # Add the gap to the value of n
    n += gap
    # Increase the gap count
    gap_count += 1
    
    # If we have traveled the gap 4 times
    if gap_count == 4:
        # Reset the counter
        gap_count = 0
        # Increase the gap by 2
        gap += 2

print(sum_diagonals)
end_time = time()
print("Time taken: ", end_time - start_time)