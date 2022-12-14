from time import time
"""
Formula = n^2 - 79n + 1601 for 0 <= n <= 79

f(n) = n^2 + an + b
-1000 < a < 1000 and   -1000 <= b <= 1000

Find the product of co-efficients a and b, which produce the maximum number of primes for consecutive values of n, starting with n = 0

The goal is that the result of the calculation, must be prime
n = 0
f(0) = 0 + 0a + b, f(0) needs to be prime, so b can only be prime numbers
n = 1
f(1) = 1 + 1a + b  , f(1) needs to be prime:
- If b is confirmed to be prime, since prime numbers are all odd between 2 and 1000, except 2
- a must be an even number (Because odd + even = odd)
- a must be odd when  1 + 1a + b, if b is prime


"""
# # Example formula = n^2 + n + 41 0 <= n <= 39
# prime_count = 0
# for n in range(0, 40):
#     calculation = int(n**2 + n + 41)
#     # If the result is a prime number
#     if is_prime(calculation) == True:
#         # Increment the prime count
#         prime_count += 1

# print(prime_count)

# # Example formula = n^2 - 79n + 1601 0 <= n <= 79
# prime_count = 0
# for n in range(0, 80):
#     calculation = int(n**2 - (79  * n) + 1601)
#     # If the result is a prime number
#     if is_prime(calculation) == True:
#         # Increment the prime count
#         prime_count += 1

# print(prime_count)

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

    print(sorted(numbers)) # Print the prime numbers list

    return numbers

def is_prime(n):
    # Look for all numbers up to sqrt(n), starting from 2 (This is because we can test all potential factors of n by only looping to sqrt(n))
    # Note: It is the absolute value because the result of the quadratic can be negative, so we will test numbers up to the abs(sqrt(n)) to see if n has any factors. If it does, then it is not prime
    for i in range(2, int(abs(n ** 0.5)) + 1):
        # If n is divisible by any numbers before it
        if n % i == 0:
            return False
    
    # If n is less than 2
    if n < 2:
        return False
    # Else
    return True

start_time = time()
b_values = sieve_of_eratosthenes(1000)

prime_count = 0
n = 0
largest_n = 0
largest_a = 0
largest_b = 0

for a in range(-1000, 1000): # -1000 < a < 1000
    # For all values of b (b must always be prime, explained in the comments)
    for b in b_values:

        # While the quadratic is a prime number
        while is_prime( int( n**2 + (a * n) + b)) == True:
            # If the n is greater than the largest n
            if n > largest_n:
                # Save the value for n, a , b and the product of the co-efficients (a and b)
                largest_n = n
                largest_a = a
                largest_b = b
                product = largest_a * largest_b

            # Keep incrementing n to get consecutive values of n
            n += 1

        # Reset n to 0, as it is no longer consecutive values of n
        n = 0

end_time = time()
print(f" Largest n: {largest_n} , Largest a: {largest_a}, Largest b: {largest_b}, Product of the two co-efficients:{product}, Time taken:{end_time - start_time}")
