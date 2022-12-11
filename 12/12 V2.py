from time import time

def generate_triangle_numbers(n):
    count = 0
    next_number = 0 
    
    # While we haven't found the nth triangle
    while count != n:
        # Next number would be the current number + the count + 2
        next_number = next_number + count + 2

        # Increment the counter
        count += 1
    
    # The next number would be pointing to the (n + 1)th term, so go back one term
    nth_number = next_number - count
    
    # Return the nth triangle number
    return nth_number


def find_prime_factors(number):
    prime_number = 2
    prime_factors = []

    # While the prime number squared is less than the number
    while prime_number ** 2 <= number:
        # Check if the number is divisible by the prime number
        if number % prime_number == 0:
            # If it is append the prime number to the prime factor list
            prime_factors.append(prime_number)
            # The number will now be the number divided by the prime number e.g. (60 // 2) == 30
            number = number // prime_number

        # If it isn't, go to the next prime number
        else:
            prime_number += 1

    # The number will be the last prime factor of the number
    prime_factors.append(number)

    return prime_factors


def count_divisors(prime_factors_list):
    """     
        The prime factorization of n is given by:
        n = p1^a1 x p2^a2 x ... x pk^ak
    
        The number of divisors of a number is given by:

        d = (a1 + 1) x (a2 + 1) x .... x (ak + 1)
    """


    # Find the number of different numbers
    unique_num_set = set(prime_factors_list) # Convert to a set to get rid of duplicate values
    num_of_unique_nums = len(unique_num_set) # Find the length of the set, giving the amount of unique numbers

    # Find the exponents of each number

    # Create a new list with the number, 
    new_list = [[list(unique_num_set)[i], 0] for i in range(0, num_of_unique_nums)]

    # For each number in the prime factors list
    for number in prime_factors_list:

        # For each pair in the new list
        for pair in new_list:

            # If the number in the prime factors list is the same as the number in the prime factors list
            if number == pair[0]:

                # Increase the quantity
                pair[1] += 1

    # Finding the number of factors of the given number
    divisors = 1
    for i in range(0, len(new_list)):
        # Find the number of factors of the number by using the second equation in the commented section
        divisors *= (new_list[i][1] + 1)

    return divisors

# Find the first triangle number with over 500 divisors
start_time = time()
n = 0
# While the number of divisors is not greater than 500
while count_divisors(find_prime_factors(generate_triangle_numbers(n))) < 500:
    # Go to the next number
    n += 1

print(generate_triangle_numbers(n))
end_time = time()
print(f"Time taken: {end_time - start_time}")