from time import time
"""
Largest pandigital 9 digit number is 987654321

- Make a number string for each value of i 
- Find the products of i * j and concatenate them to the string
- Convert the string into a set.
"""

greatest_pandigital = 0
start_time = time()
for i in range(0, 9327 + 1):
    # Create an empty string
    pandigital_string = ""
    
    for j in range(1, 9):

        # If the length of the pandigital string plus the string of the product is less than 10
        if len(pandigital_string + str(i * j)) < 10:
            # Add the string of the product to the pandigital string
            pandigital_string += str(i *j)

            # If the length of the pandigital string is 9 (9 digits long) and it all of the digits are unique 
            if len(set(pandigital_string)) == 9 and len(pandigital_string) == 9:

                flag = True # Set the flag as True (As to whether it is a valid pandigital)
                for x in range(1, 9 + 1):
                    # If any of the numbers from 1 to 9 are not in the set of the pandigital string, then it is not a pandigital number
                    if str(x) not in set(pandigital_string):
                        flag = False

                # Check if the number is greater than the greatest pandigital we have found so far
                if (int(pandigital_string) > greatest_pandigital) and flag == True:
                    # Set the current pandigital as the greatest pandigital number we have found so far
                    greatest_pandigital = int(pandigital_string)
                    print("New greatest pandigital", greatest_pandigital)

end_time = time()
print("Greatest pandigital:", greatest_pandigital)
print("Time taken: ", end_time - start_time)