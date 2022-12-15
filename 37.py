from ast import ClassDef
from time import time
def sieve_of_eratosthenes(n):
    # Create a list of numbers from 2 to n
    numbers = [num for num in range(2, n)]

    for i in range(2, int((n ** 0.5) + 1)):
        # If the number is an integer (meaning that it isn't a composite number, otherwise it would be a Boolean value)
        if type(numbers[i - 2]) == int:

            # For numbers i till n, mark all multiples of i as False
            for x in range(i, n, i):

                # If x is any multiple of i, but not i (e.g. 48 would be a multiple of 7, but do not set 7 as False)
                if x != i: 

                    # Set the multiple as False
                    numbers[x - 2] = False

    # Convert the list into a set to get rid of all False statements except one
    numbers = list(set(numbers)) # Convert the set back to a list
    numbers.remove(False) # Remove the last False statement
    
    return sorted(numbers)

prime_numbers = sieve_of_eratosthenes(1000000)

print(prime_numbers)
""" First version """
# def truncate_num(n):
#     num_string = str(n)
#     possible_primes = []
#     """ A 4 digit number would need to be truncated 3 times, so the end would be len(num_string) - 1"""
#     # Truncate left to right
#     for i in range(0, len(num_string) - 1):
#         possible_primes.append(num_string)
#         num_string = num_string[1:]
#         # If this current truncated value is not in prime numbers
#         if int(num_string) not in prime_numbers:
#             return False
            

#     # Declare the num string again
#     num_string = str(n)

#     # Truncate right to left
#     for i in range(0, len(num_string) - 1):
#         num_string = num_string[:-1]
#         possible_primes.append(num_string)
#         # If this current truncated value is not in prime numbers
#         if int(num_string) not in prime_numbers:
#             return False
    
#     return True

"""Second version"""
def truncate_num(n):
    num_string = str(n)
    possible_primes = [num_string] # Add num_string to the possible primes
    """ 
    This works by simultaneously taking the first i and last i digits in each iteration. E.g:
    The first and last digits:
    3  7
    The first two digits and the last 2 digits:
    37  97

    The first 3 digits and the last 3 digits
    379 797

    """
    for i in range(1, len(num_string)): # Start at index 1
        # Add the first i digits of the num string to the list
        possible_primes.append(num_string[:i])
        # Add the last i digits of the num string to the list
        possible_primes.append(num_string[i:])
        # Check if either of the numbers are not in prime numbers, if one of them is False, then it means that n is not truncatable from both left to right and right to left
        if int(num_string[:i]) not in prime_numbers or int(num_string[i:]) not in prime_numbers:
            return False

    return True

print(truncate_num(739397))

# There are only 11 primes that are truncatable from left to right
trunc_prime_count = 0
i = 4 # Start at index 4, as 2, 3, 5 and 7 are not considered to be truncatable primes
trunc_prime_sum = 0
start_time = time()

# While we haven't found the 11 primes that are truncatable from both left to right and right to left, or we have reached the end of our list of primes.
while trunc_prime_count != 11 or i != len(prime_numbers) - 1:

    # If the function returns true, it is a prime number truncatable from both left to right and right to left
    if truncate_num(prime_numbers[i]):
        print(prime_numbers[i])
        # Increase the number of primes that are truncatable from both left to right and right to left
        trunc_prime_count += 1
        # Add the prime number to the sum
        trunc_prime_sum += prime_numbers[i]

    # Increase the index
    i += 1

print("Sum: ", trunc_prime_sum)
end_time = time()
print("Time taken: ", end_time - start_time)