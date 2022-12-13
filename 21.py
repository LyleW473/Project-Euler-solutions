from time import time

def sum_proper_divisors(n):
    sum = 0
    # Iterate to the square root of n, we can find all factors by only iterating to sqrt(n)
    for i in range(1, int(n**0.5)):
        # If n is divisible by i
        if n % i == 0:
            # Add the factor to the sum
            sum += i

            # The other factor would be given by dividing n by the factor that we just found
            if int(n // i ) != n: # As long as the factor isn't itself (e.g. if n = 220, do not include 220)
                sum += int(n // i)

    return sum


def sum_amicable_numbers(upper_boundary):
    start_time = time()
    sum = 0

    # For all values a to the upper boundary
    for a in range(upper_boundary):
        # Create a variable which is the sum of the divisors of a
        b = sum_proper_divisors(a)
        # Check if the the sum of the divisors of b is equal to a, and if a is not equal to b
        if sum_proper_divisors(b) == a and a != b:
            # Add either a or b
            sum += a
    end_time = time()
    return sum , end_time - start_time
    

print(sum_amicable_numbers(10000))
