from time import time
""" 
- Find all integers less than 28123 that cannot be written as the sum of two abundant numbers
- Abundant number = If the sum of n's proper divsors is greater than n
- 12 is the smallest abundant number

- Every multiple of a perfect number is abundant
- Every multiple of an abundant number is abundant

"""
def sum_of_divisors(n):
    factors_list = []
    sum = 0
    # Iterate to the square root of n (This will still allow us to find all factors of n)
    for i in range(1, int(n ** 0.5) + 1):
        
        # If n is divisible by i
        if n % i == 0:
            # Add the factor
            factors_list.append(i)
            sum += i

            # Find the other factor of n (e.g. if n = 20, i = 4, then n // i would be 5, so append 5), but if (n // i) == n, i.e. 20 // 1, don't append 20
            if int(n // i) != n and (n // i) not in factors_list: # The same applies for if the factor is already inside the list, then don't append it.
                # Add the factor
                factors_list.append(n // i)
                sum += (n // i)

    # Return the sum of all proper divisors and n
    return sum, n, factors_list

start_time = time()

# # Find all the abundant numbers from 
# abundant_numbers_list = [False] * (28124 - 11)
# for n in range(11, 28124):
#     # If the sum of the proper divisors of n is greater than or equal to n, it is an abundant number, or a perfect number
#     if sum_of_divisors(n)[0] >= sum_of_divisors(n)[1]:

#         # Append the number to the list if it is an abundant number, not a perfect number
#         if sum_of_divisors(n)[0] > sum_of_divisors(n)[1]:
#             abundant_numbers_list.append(n)

#         # Iterate for all multiples of n, starting from n x 2, with step n (For perfect and abundant numbers)
#         for i in range(n * 2, 28124, n):
#             abundant_numbers_list[i - 11] = i

# # Convert it to a set to remove duplicate "False" values, and then remove the final False value. Sort the list
# abundant_numbers_list = sorted(list(set(abundant_numbers_list)))
# abundant_numbers_list.remove(False)
# print(abundant_numbers_list)
# print(len(abundant_numbers_list))

# Create a list of abundant numbers (If the sum of the factors of n are greater than n, it is an abundant number)
abundant_numbers_list = [n for n in range(11, 28124) if sum_of_divisors(n)[0] > sum_of_divisors(n)[1]] # This code serves the same purpose as the code above


# Finding the all the numbers that can be written as the sum of abundant sums
sum_abundant_nums_list = []
# For each item in the list of abundant numbers
for item in abundant_numbers_list:
    # Loop from the starting item of the list to end item
    for j in range(0, len(abundant_numbers_list)):

        # If the sum of the two abundant numbers are above 28123, we know that the number can be expressed as a sum of two abundant numbers, so break out of the loop
        if (item + abundant_numbers_list[j]) > 28123:
            break
        
        # Append the sum of the two abundant numbers
        sum_abundant_nums_list.append(item + abundant_numbers_list[j])
        

# Convert the list into a set(gets rid of duplicate values if there are any), convert it back into the list and then sort the list.
sum_abundant_nums_list = sorted(list(set(sum_abundant_nums_list)))

print(sum_abundant_nums_list)
print("length", len(sum_abundant_nums_list))


# Finding all the numbers that cannot be written as the sum of two abundant numbers
non_sum_of_two_abundant_numbers_integers = []
sum_of_pos_ints = 0
starting_item = 0
item_index = 0
starting_item = sum_abundant_nums_list[0]

# Find all numbers less than 28123 that cannot be written as the sum of two abundant numbers
for i in range(1, 28123):
    # If the number is not equal to the current number that can be written as the sum of two abundant numbers, and if the index is not pointing to the last item to the list
    if i == starting_item and item_index < len(sum_abundant_nums_list) - 1:
        # Increase the index
        item_index += 1
        # Set the current number that can be written as the sum of two abundant numbers to be the next item in the list
        starting_item = sum_abundant_nums_list[item_index]
        # Skip to the next iteration
        continue
    
    # Add the number to the sum of positive integers that cannot be written as the sum of two abundant numbers
    sum_of_pos_ints += i
    # Add it to the list
    non_sum_of_two_abundant_numbers_integers.append(i)

print(non_sum_of_two_abundant_numbers_integers)
print(sum_of_pos_ints)
end_time = time()
print("Time taken: ", end_time - start_time)


################################
# This code serves the same purpose as the code above

# # For each item in the list
# for item in sum_abundant_nums_list:

#     # Loop from the previous number that can be expressed as a sum of two abundant numbers + 1, to the current number.
#     for i in range(starting_item + 1, item):
#         # Add it to the list of numbers that cannot be written as the sum of two abundant numbers
#         non_sum_of_two_abundant_numbers_integers.append(i)
#         # Add it to the sum
#         sum_of_pos_ints += i

#     # Set the starting item to be the current item. Loop from e.g. 24 to the next integer that can be expressed as the sum of two abundant sums.
#     starting_item = item

# print(non_sum_of_two_abundant_numbers_integers)  
# print(sum_of_pos_ints)
# end_time = time()
# print("Time taken: ", end_time - start_time)