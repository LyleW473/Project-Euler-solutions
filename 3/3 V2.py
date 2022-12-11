from time import time

def find_prime_factors(number):
    start_time = time()
    prime_number = 2 # The smallest prime number would be 2

    # While the prime number squared is less than the number
    while prime_number ** 2 <= number: 
    
        # If the number is divisible by the prime number
        if number % prime_number == 0:
            # The number will now be the number divided by the prime number e.g. 30 // 2 = 15
            number = number // prime_number

        # If the number is not divisible, increment the prime number
        else:
            prime_number += 1

    # The number should be the last prime factor, which would be the largest prime factor
    greatest_prime_factor = number

    end_time = time()
    return greatest_prime_factor, (end_time - start_time)

greatest_prime_factor, time_taken = find_prime_factors(600851475143)
print(greatest_prime_factor, time_taken)