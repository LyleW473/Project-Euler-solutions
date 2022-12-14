from time import time
"""
The largest value for a single digit in the number is 9. 9^5 = 59049

5 digits x 9^5 = 295245 (Only 5 digit numbers up to 295245 and below can be written as the sum of fiifth powers of their digits)
7 digits x 9^5 = 413343 (A seven digit number cannot be written as the sum of the fifth powers of their digits as the maximum the sum can be is only six digits)

"""
start_time = time()
final_sum = 0
for i in range(2, 295245+ 1):

    # Reset sum for each value of i
    sum = 0
    for j in range(0, len(str(i))):
        # Add the digit to the power of 4 to the sum
        sum += int(int(str(i)[j]) ** 5)

    # Check if the sum is the same as the numbers
    if sum == i:
        print(i)
        # Add the number to the final sum
        final_sum += i

end_time = time()
print("Final sum: ", final_sum, "Time taken: ", end_time - start_time)