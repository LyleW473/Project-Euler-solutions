from time import time
""" 
n = 585
f"{n:b}" used to convert to base 2 (binary).
"""

sum = 0
start_time = time()
for n in range(0, 1000000 + 1):
    # If the number in base 2 has an even number of digits
    if len(str(f"{n:b}")) % 2 == 0:

        # If the first half of the string is the same as the second half of the string reversed
        if str(f"{n:b}")[:len(str(f"{n:b}")) // 2]  == str(f"{n:b}")[(len(str(f"{n:b}")) // 2):][::-1]:

            # Check base 10 afterwards

            # If the string in base 10 has an even number of digits
            if len(str(n)) % 2 == 0:

                # If the first half of the string is the same as the second half of the string reversed
                if str(n)[: len(str(n)) // 2] == str(n)[(len(str(n)) // 2) :][::-1]:
                    print(n, str(f"{n:b}"))

                    # Add the number to the sum
                    sum += n

            # If the string in base 10 has an odd number of digits
            elif len(str(n)) % 2 != 0:
                # If the left side of the string (from the middle item) is the same as the right side of the string (from the middle item) reversed
                if str(n)[: len(str(n)) // 2] == str(n)[(len(str(n)) // 2) + 1:][::-1]:
                    print(n, str(f"{n:b}"))

                    # Add the number to the sum
                    sum += n    
    
    # If the number in base 2 
    elif len(str(f"{n:b}")) % 2 != 0:

        # If the left side of the string (from the middle item) is the same as the right side of the string (from the middle item) reversed
        if str(f"{n:b}")[:len(str(f"{n:b}")) // 2]  == str(f"{n:b}")[(len(str(f"{n:b}")) // 2) + 1:][::-1]:
            
            # Check base 10 afterwards

            # If the string in base 10 has an even number of digits
            if len(str(n)) % 2 == 0:

                # If the first half of the string is the same as the second half of the string reversed
                if str(n)[: len(str(n)) // 2] == str(n)[(len(str(n)) // 2) :][::-1]:
                    print(n, str(f"{n:b}"))

                    # Add the number to the sum
                    sum += n

            # If the string in base 10 has an odd number of digits
            elif len(str(n)) % 2 != 0:
                # If the left side of the string (from the middle item) is the same as the right side of the string (from the middle item) reversed
                if str(n)[: len(str(n)) // 2] == str(n)[(len(str(n)) // 2) + 1:][::-1]:
                    print(n, str(f"{n:b}"))

                    # Add the number to the sum
                    sum += n    

    
print("Sum: ", sum)
end_time = time()
print("Time taken:", end_time - start_time)