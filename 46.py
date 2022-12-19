from time import time

def generate_odd_composite_numbers(n):  

    composite_set = set()
    prime_list = [num for num in range(2, n + 2)]

    for i in range(2, int(n ** 0.5), 1):
        
        # Add all the numbers that are composite from 
        for j in range(i ** 2, n + 2, i):
            # If the number is odd
            if j % 2 != 0:
                composite_set.add(j) 

            # Mark all these numbers as composite (regardless whether they are even or odd)
            prime_list[j - 2] = False
    
    # Sort the lists, removing the False values
    prime_list = sorted(prime_list)
    composite_list = sorted(list(composite_set))
    slicing_index = 0

    # Decrement from the last item in the primes list until we found the first boolean value
    for x in range(len(prime_list) - 1, 0, -1):

        # When we found the first boolean, assign the slicing index slice the list, keeping everything above that index
        if type(prime_list[x]) == bool:
            slicing_index = x
            break

    # Slice the list, keeping everything above the slicing index
    prime_list = prime_list[slicing_index + 1:]

    return composite_list, prime_list

def find_smallest_odd_composite():
    start_time = time()
    goldbach_numbers_list = []
    prime_number_index = 0
    odd_composite_numbers_list_index = 0
    
    # Generate the prime and composite numbers up to 6000
    odd_composite_numbers_list, prime_list = generate_odd_composite_numbers(6000)

    # For all composite numbers
    while odd_composite_numbers_list_index != len(odd_composite_numbers_list) - 1:

        # Reset the temporary list for every new odd composite number
        temp_list = []
        
        # While 7 < 9:
        while prime_list[prime_number_index] < odd_composite_numbers_list[odd_composite_numbers_list_index] :

            # Find the difference between the prime and the composite number, so that we can find out what squares we should find
            difference = odd_composite_numbers_list[odd_composite_numbers_list_index] - prime_list[prime_number_index]
            
            # Find the maximum value a square number can have for the composite number
            for square in range(1, int(difference ** 0.5) + 1): # maximum_square = int(difference ** 0.5) 
                
                # If the odd composite number can be written as the sum of a prime  E.g. If 9 = 7 + (2 x 1^2)
                if odd_composite_numbers_list[odd_composite_numbers_list_index] == prime_list[prime_number_index] + (2 * (square ** 2)):
                    #print(f"{odd_composite_numbers_list[odd_composite_numbers_list_index]} = {prime_list[prime_number_index]} + (2 * {square}^2) ")

                    # Add the value to the temp list
                    temp_list.append( (odd_composite_numbers_list[odd_composite_numbers_list_index], prime_list[prime_number_index], square))

            # Go to the next highest prime number less than the composite number
            prime_number_index += 1

        # If the temp list is empty, this means no solutions were found
        if len(temp_list) == 0:
            # Return the smallest odd composite that cannot be written as the sum of a prime and twice a square
            end_time = time()
            return odd_composite_numbers_list[odd_composite_numbers_list_index], end_time - start_time

        # Otherwise
        else:
            # Add the last item in the goldbach numbers list
            goldbach_numbers_list.append(temp_list[-1]) 

            # Go to next composite number
            odd_composite_numbers_list_index += 1

            # Reset prime number index
            prime_number_index = 0

smallest_odd_composite, time_taken = find_smallest_odd_composite()
print(f"Smallest odd composite: {smallest_odd_composite}\nTime taken: {time_taken}")