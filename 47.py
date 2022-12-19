from time import time

def generate_four_distinct_prime_factors_list(amount):
    four_distinct_prime_factors_list = []
    n = 7
    while n <= amount:

        if type(four_distinct_prime_factors(n)) == int:
            four_distinct_prime_factors_list.append(four_distinct_prime_factors(n))

        n += 1

    print("n = ",  n)
    return four_distinct_prime_factors_list

def four_distinct_prime_factors(n):
    original_number = n
    prime_factors_set = set()
    prime_number = 2

    while prime_number < n:

        # If n is divisible by the prime number
        if n % prime_number == 0:
            # Divide the number by the prime number
            n /= prime_number
            # Add the prime factors to the set
            prime_factors_set.add(prime_number)

            if len(prime_factors_set) > 4:
                break
            
        # Otherwise
        else:
            # Increment the prime numebr
            prime_number += 1

    # The final number will be the last prime factor
    prime_factors_set.add(int(n))

    if len(prime_factors_set) == 4:
        return original_number


def find_consecutive_integers_with_FDPF():
    start_time = time()

    consecutive_counter = 0 
    four_distinct_prime_factors_list = generate_four_distinct_prime_factors_list(150000)
    print(four_distinct_prime_factors_list)
    print(len(four_distinct_prime_factors_list))
    end_time = time()
    four_consecutive_integers_list = []
    print("Time taken: ", end_time - start_time)

    for i in range(0, len(four_distinct_prime_factors_list) - 1, 1):
        # If the difference between the item in front of the current item and the current item is one, then they are next to each other
        if (four_distinct_prime_factors_list[i + 1] - four_distinct_prime_factors_list[i]) == 1:

            # Increment the counter
            consecutive_counter += 1
            # Add the integer to the list
            four_consecutive_integers_list.append(four_distinct_prime_factors_list[i])

            # Counter is at 3 because we are looking at integers in pairs e.g. 11 and 12, 12 and 13, 13 and 14, If all three pairs have a difference of 1, it means that they are consecutive
            if consecutive_counter == 3:
                four_consecutive_integers_list.append(four_distinct_prime_factors_list[i + 1])
                print("Four consecutive integers: ", four_consecutive_integers_list)
                end_time = time()
                print("Time taken: ", end_time - start_time)
                break

        else:
            # Reset the integers list
            four_consecutive_integers_list = []
            # Reset the counter
            consecutive_counter = 0 


find_consecutive_integers_with_FDPF()

