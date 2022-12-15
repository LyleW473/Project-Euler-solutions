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

""" First version of the rotate function """
# def rotate(n):
#     num_string = list(str(n))
#     possible_primes = []

#     # Do len(num_string) rotations. Sending the first digit to the back of the list each rotation
#     # E.g. 197, 971, 719
#     for i in range(0, len(num_string)):
#         possible_primes.append(str(num_string.copy()))
#         # Send the first digit to the back
#         first_digit = num_string.pop(0)
#         num_string.append(first_digit) 

#     # Create a list of possible primes so that they can be checked for whether they are prime
#     possible_primes = str(possible_primes).replace("[", "").replace("]", "").replace("'", "").replace(",", "").replace(" ", "")[1:-1].split('""')
#     #print(possible_primes)

#     # Check if each prime in the possible primes list is prime
#     for i in range(0, len(possible_primes)):
#         #print(possible_primes[i])
#         # The moment that one number is proven to not be prime
#         if int(possible_primes[i]) not in prime_numbers:
#             return False

#     # Else return True
#     return True

"""Second version of the rotate function"""
# def rotate(n):
#     num_string = str(n)
#     possible_primes = []
#     # Do len(num_string) rotations. Sending the first digit to the back of the list each rotation
#     for i in range(0, len(num_string)):
#         possible_primes.append(str(num_string))

#         # Send the first item of the string to the back of the string
#         num_string = num_string[1:] + num_string[0]

#     # Check if each prime in the possible primes list is prime
#     for i in range(0, len(possible_primes)):
#         #print(possible_primes[i])
#         # The moment that one number is proven to not be prime
#         if int(possible_primes[i]) not in prime_numbers:
#             return False
#     # Else return True
#     return True

""" Third version of the rotate function"""
def rotate(n):
    num_string = str(n)
    # Do len(num_string) rotations. Sending the first digit to the back of the list each rotation
    for i in range(0, len(num_string)):
        # Send the first item of the string to the end of the string
        num_string = num_string[1:] + num_string[0]
        # Check if the current prime number we just rotated to is in the prime numbers list
        if int(num_string) not in prime_numbers:
            # If it isn't then we just exit out here
            return False
    # Otherwise, n is a circular prime as all rotations are prime
    return True


circular_prime_counter = 0
start_time = time()
print("Started")
# For each item in the prime numbers list
for item in prime_numbers:
    # If all rotations of the prime number are prime
    if rotate(item) == True:
        # Increase the counter
        circular_prime_counter += 1

print("Number of circular primes: ", circular_prime_counter)
end_time = time()
print("Time taken: ", end_time - start_time)