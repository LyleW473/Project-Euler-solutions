from time import time

"""
To shorten the amount of numbers we have to check, if a number is divisible by 20, they will also be divisible by 10, 5, 2.
We can do this with more numbers and we would only have to check numbers [20, 19, 18, 17, 16, 14, 13, 11]

"""

number = 2520
found = False
index = 20

start_time = time()
while found == False:

    # If the number is not divisible by 20
    if number % 20 != 0:
        # Add 2520 to the current number
        # Note: This is because the number must be evenly divisible by all numbers one to 10, the first of which is 2520. And any number that is divisible by 2520, is divisible by numbers from 1 to 10.
        number += 2520

    # If the number is divisible by 20
    else: 
        # Decrement the index
        index -= 1
        # If the number is not divisible by one of the indexes before 20 e.g. 9
        if number % index != 0:
            # Go to the next number
            number += 2520
            # Reset the index
            index = 20

        # If the number is divisilbe by the index and the index is 11, it means it was divisible by all indexes
        if number % index == 0 and index == 11:
            # Print the number
            print(number)
            # Set found to True
            found = True
            
            end_time = time()


print(end_time - start_time)

