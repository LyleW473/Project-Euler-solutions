from time import time

def find_primes(amount):
    """ Finds prime numbers up to an amount """

    # Create a list of amount elements
    prime_numbers = [num for num in range(2, amount + 2)]

    
    for i in range(2, int(amount ** 0.5)):

        for j in range(i ** 2, amount + 2, i):
            
            # Mark composite numbers as False
            prime_numbers[j-2] = False

    # Sort the list, removing duplicate "False" values
    prime_numbers = sorted(list(set(prime_numbers)))
    # Remove the final "False" value
    prime_numbers.remove(False)

    return prime_numbers

def four_distinct_prime_factors(n, primes_list):
    prime_factors_set = set()
    primes_list = primes_list
    prime_list_index = 0

    # While the prime number is less than n and the prime number isn't the last item in the primes list
    while primes_list[prime_list_index] < n and prime_list_index < len(primes_list):

        # If n is divisible by the prime number
        if n % primes_list[prime_list_index] == 0:
            # Divide the number by the prime number
            n /= primes_list[prime_list_index]
            # Add the prime factors to the set
            prime_factors_set.add(primes_list[prime_list_index])

            if len(prime_factors_set) > 4:
                break
            
        # Otherwise
        else:
            # Increment the prime number index to go to the next prime number
            prime_list_index += 1

    # The final number will be the last prime factor
    prime_factors_set.add(int(n))

    if len(prime_factors_set) == 4:
        return True

def generate_four_distinct_prime_factors_list(amount, primes_list):
    """ 
        Finds all the composite numbers up to {amount}, to have multiple prime factors, the numbers must be composite. Checks whether it has 4 distinct prime factors, adding it
        to the list if they do.

        Create a list for primes which will be used in the 'four_distinct_prime_factors' list, because as the number grows, incrementing by one is inefficient, so it would be 
        quicker for 'prime_number' to be only prime numbers.
        
    """
    four_distinct_prime_factors_list = []

    for i in range(2, int(amount ** 0.5) ):
        for j in range(i ** 2, amount + 1, i):
            
            # If the number has 4 distinct factors
            if four_distinct_prime_factors(j, primes_list) == True:
                
                # Add the number to the four distinct values
                four_distinct_prime_factors_list.append(j)

    # Sort the list and remove duplicate values
    four_distinct_prime_factors_list =  sorted(list(set(four_distinct_prime_factors_list)))

    return four_distinct_prime_factors_list

def find_consecutive_integers_with_FDPF(amount):
    start_time = time()
    consecutive_counter = 0 
    # Generate a list with only integers that have four distinct prime factors
    four_distinct_prime_factors_list = generate_four_distinct_prime_factors_list(amount, find_primes(amount // 2))
    four_consecutive_integers_list = []

    for i in range(0, len(four_distinct_prime_factors_list) - 1, 1):
        # If the difference between the item in front of the current item and the current item is one, then they are next to each other
        if (four_distinct_prime_factors_list[i + 1] - four_distinct_prime_factors_list[i]) == 1:

            # Increment the counter
            consecutive_counter += 1
            # Add the integer to the list
            four_consecutive_integers_list.append(four_distinct_prime_factors_list[i])

            # Counter is at 3 because we are looking at integers in pairs e.g. 11 and 12, 12 and 13, 13 and 14, If all three pairs have a difference of 1, it means that they are consecutive
            if consecutive_counter == 3:
                # Add the last remaining consecutive integer
                four_consecutive_integers_list.append(four_distinct_prime_factors_list[i + 1])
                # Return the consecutive integers list
                end_time = time()
                return four_consecutive_integers_list, end_time - start_time
        else:
            # Reset the integers list
            four_consecutive_integers_list = []
            # Reset the counter
            consecutive_counter = 0 

four_consecutive_integers_list, time_taken = find_consecutive_integers_with_FDPF(150000)
print(f"Four consecutive integers list: {four_consecutive_integers_list}\nTime taken: {time_taken}")