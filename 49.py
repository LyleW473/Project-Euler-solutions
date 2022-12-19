from time import time
"""
Find numbers that have the same digits, the same difference between each consecutive term, and are all primes:
"""

def find_primes():
    # Create a list of elements to store the prime numbers up to 10000
    prime_numbers = [num for num in range(2, 9999 + 2)]

    for b in range(2, int(9999 ** 0.5)): 

        for c in range(b ** 2, 9999 + 2, b):
            
            # Mark composite numbers as False
            prime_numbers[c - 2] = False

    # Sort the list, removing duplicate "False" values
    prime_list = sorted(list(set(prime_numbers)))
    prime_list.remove(False)

    # Remove items below 1009 # 1009 is the first 4 digit prime
    slicing_index = prime_list.index(1009)

    return prime_list[slicing_index:]

# Used a prime set for faster access time, used a prime list to iterate from the first 4 digit prime, going upwards 
primes_list = sorted(find_primes())
primes_set = set(primes_list)


def solve():
    start_time = time()

    for prime1 in primes_list:

        for prime2 in primes_set:

            for prime3 in primes_set:
                
                # If all 3 primes have the same digits
                if set(str(prime1)) == set(str(prime2)) and set(str(prime2)) == set(str(prime3)) and set(str(prime1)) == set(str(prime3)):
                    
                    # If none of the primes are the same
                    if prime1 != prime2 and prime2 != prime3 and prime1 != prime3 and prime1 != 1487:
                        # Order them in terms of their value:
                        #print("1", prime1, "2", prime2, "3", prime3)
                        values_list = sorted([prime1, prime2, prime3])

                        # If the difference between the 2nd and the 1st prime is the same as the difference between the 3rd and the 2nd
                        if abs(prime2 - prime1) == abs(prime3 - prime2):

                            # Find the 12 digit number found by concatenating the three terms in the sequence
                            three_terms_string = ""
                            for value in values_list:
                                # Concatenate each term to the string
                                three_terms_string += str(value)

                            end_time = time()
                            return three_terms_string, values_list, end_time - start_time
           
three_terms_string, values_list, time_taken = solve()
print(f"String: {int(three_terms_string)}\nAll three terms: {values_list}\nTime taken: {time_taken}")

def solve_v2():
    start_time = time()

    for a in range(len(primes_list)):

        for b in range(a, len(primes_list)):

            for c in range(b, len(primes_list)):
                
                if set(str(primes_list[a])) == set(str(primes_list[b])) and set(str(primes_list[b])) == set(str(primes_list[c])) and set(str(primes_list[a])) == set(str(primes_list[c])):
                    # If all 3 primes have the same digits
                    if primes_list[a] != primes_list[b] and primes_list[b] != primes_list[c] and primes_list[a] != primes_list[c] and primes_list[a] != 1487:
                        # Order them in terms of their value:
                        values_list = sorted([primes_list[a], primes_list[b], primes_list[c]])

                        # If the difference between the 2nd and the 1st prime is the same as the difference between the 3rd and the 2nd
                        if abs(primes_list[b] - primes_list[a]) == abs(primes_list[c] - primes_list[b]):

                            # Find the 12 digit number found by concatenating the three terms in the sequence
                            three_terms_string = ""
                            for value in values_list:
                                # Concatenate each term to the string
                                three_terms_string += str(value)

                            end_time = time()
                            return three_terms_string, values_list, end_time - start_time

three_terms_string, values_list, time_taken = solve_v2()
print(f"String: {int(three_terms_string)}\nAll three terms: {values_list}\nTime taken: {time_taken}")