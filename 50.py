from time import time

def sieve(n):
    sieve = [True] * n
    prime_list = []

    # Check for prime from numbers 2 to input number
    for p in range(2, n):
        # If the item is set to True
        if sieve[p]: 
            # Add it to the prime list
            prime_list.append(p)

            # Starting from p^2, mark all multiples of p as False (as they are composite numbers)
            for i in range(p*p, n, p): 
                sieve[i] = False

    # Return a list of primes and a set of primes
    return prime_list, set(prime_list)

def solve():
    start_time = time()
    # Generate a list and set of prime numbers under 1,000,000
    prime_list, prime_set = sieve(1000000)
    greatest_length = 0
    
    # For each prime in the list
    for i in range(0, len(prime_list)):

        # From the first prime value to the prime value we are looking at (i.e. prime_list[i])
        for j in range(0, i):
            
            # If we have found a consecutive chain that is already e.g. 20 terms long, skip values of j until there is a gap of 21, so that we only check for sums greater than 20 terms long
            if (i - j) >= greatest_length:

                # Sum up the range of between j and i
                possible_prime = sum(prime_list[j : i])

                # If the possible prime is past 1,000,000, end the function
                if possible_prime > 1000000:
                    end_time = time()
                    # Return: The prime that can be written as the sum of the most consecutive primes, how many consecutive primes, and the prime numbers that add up to the sum (and time taken)
                    return prime_with_greatest_length, greatest_length, greatest_list, end_time - start_time
                        
                # Check if the sum is in the prime set (Used set for faster access time)
                if possible_prime in prime_set:

                    # If it is prime, check how if the length of the consecutive numbers summed to make the sum is the greatest we have found
                    if len(prime_list[j:i]) > greatest_length:
                        # Save how many consecutive primes make up the sum
                        greatest_length = len(prime_list[j:i])
                        # Save the prime number that can be written as the sum of these consecutive primes
                        prime_with_greatest_length = possible_prime
                        # Save the consecutive primes that sum up to the prime
                        greatest_list = prime_list[j:i]

            # If the gap isn't e.g. 20 terms long, skip the values
            else:
                break

prime_with_greatest_length, greatest_length, greatest_list, time_taken = solve()
print(f"Greatest prime: {prime_with_greatest_length}\nGreatest length: {greatest_length}\nTime taken: {time_taken}")
print(f"List of consecutive numbers:\n", greatest_list)


            





        