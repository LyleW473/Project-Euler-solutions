from time import time
""" 
Tn = n(n + 1) / 2  
Pn = n(3n - 1) / 2
Hn = n(2n - 1) 

Tn = (1/2)n^2 + (1/2)n
Pn = (3/2)n^2 - (3/2)n
Hn = 2n^2 - n

Generate a hexagonal number, check if it is also a triangular and pentagonal number.
"""

def generate_hexagonal_number(n):
    # Return the hexagonal number based on n
    return n * ((2 * n) - 1)

def find_next_number():
    start_time = time()

    n = 143 + 1 # The 143rd hexagonal number is 40755
    while True:
        
        # Generate the next hexagonal number
        hexagonal_number = generate_hexagonal_number(n)  

        # triangular_solution = ( -1 + ( (1)** 2 - (4 * 1 * ( (hexagonal_number) * 2 * -1 ))) ** 0.5 ) / (2 * 1)
        # pentagonal_solution = ( 1 + ( (-1)** 2 - (4 * 3 * ( (hexagonal_number) * 2 * -1 ))) ** 0.5 ) / (2 * 3)

        # Check if the hexagonal number is also a triangular and pentagonal
        if str(( -1 + ( (1)** 2 - (4 * 1 * ( (hexagonal_number) * 2 * -1 ))) ** 0.5 ) / (2 * 1))[-1] == "0" and str(( 1 + ( (-1)** 2 - (4 * 3 * ( (hexagonal_number) * 2 * -1 ))) ** 0.5 ) / (2 * 3))[-1] == "0":
            # Print the next triangle number that is also pentagonal and hexagonal
            print("Number: ", hexagonal_number)
            print("n: ", n)
            # Exit the while loop
            end_time = time()
            print("Time taken: ", end_time - start_time)
            break

        # If it isn't also triangular and pentagonal
        else:
            # Go to the next hexagonal number
            n += 1

find_next_number()