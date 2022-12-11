from time import time

def check_if_prime(number):
    count = 0
    # If the number is 2, return True
    if number == 2:
        return True

    # If the number is less than 2, return False
    if number < 2:
        return False

    for i in range(2, int((number * 0.5) + 1)): # Iterate from 2 till the sqrt(number). We can find all factors by iterating till the sqrt of the number.
        # If the number is divisible by i
        if number % i == 0: 
            count += 1
            # If the count is greater than 0, it means that it has a factor other than itself, and 1
            if count > 0:
                return False

    # Else return True
    return True


def find_nth_prime(n):
    start_time = time()

    prime_number_count = 0
    number = 0

    # While we haven't found the nth prime number
    while prime_number_count != n:
        # Increment the number
        number += 1
        # Check if the number is prime
        if check_if_prime(number) == True:
            # Increment the counter
            prime_number_count += 1

    end_time = time()
    # Return the nth prime number
    return number, (end_time - start_time)


nth_prime_number, time_taken = find_nth_prime(10001)
print(nth_prime_number, time_taken)