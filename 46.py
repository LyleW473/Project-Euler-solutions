def generate_odd_composite_numbers(n):  

    composite_set = set()  
    prime_list = [num for num in range(2, n + 2)]

    
    for i in range(2, int(n ** 0.5), 1):
        
        # Add all the numbers that are composite from 
        for j in range(i * i, n + 2, i):

            # If the number is odd
            if j % 2 != 0:
                composite_set.add(j) 
            # Mark all these numbers as composite (regardless whether they are even or odd)
            prime_list[j - 2] = False
    
    # Sort the list, removing the False values
    prime_list = sorted(prime_list)
    slicing_index = 0

    # Decrement from the last item in the primes list until we found the first boolean value
    for x in range(len(prime_list) - 1, 0, -1):

        # When we found the first boolean, assign the slicing index slice the list, keeping everything above that index
        if type(prime_list[x]) == bool:
            slicing_index = x
            break

    # Slice the list, keeping everything above the slicing index
    prime_list = prime_list[slicing_index + 1:]

    return composite_set, prime_list

odd_composite_numbers_set, prime_list = generate_odd_composite_numbers(1000)
print(odd_composite_numbers_set)
print(prime_list)