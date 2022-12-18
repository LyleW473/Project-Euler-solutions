from time import time
"""
Pn = n(3n - 1) / 2

1, 5, 12, 22, 35, 51, 70, 92, 117, 145

d = 4, 7, 10, 13, 16, 19, 22, 25, 28
Difference grows as the pentagonal number grows, so that means the first pair found will also have the "minimised difference".

Test all the pentagonal numbers with each other until the last possible pair is checked e.g.:
- Start at number 12, check its value against every other value: i.e. 12 and 1, 12 and 5, 12 and 22 etc. (Can check higher values because the sum of the two numbers will
    always be positive, but the equation for difference is |Pk - Pj| (modulus) , so Pj can be greater than Pk, which is 12 in this case))
"""

def find_pentagonal_numbers(amount_of_pentagonal_numbers, n = 1): # Starts finding P1, then P2, P3, etc..
    pentagonal_numbers_list = []

    # While we haven't found n pentagonal numbers
    while n != amount_of_pentagonal_numbers:
        # Pn = n(3n - 1) / 2
        # Add the pentagonal number to the list
        pentagonal_numbers_list.append(  (n * ((3 * n) - 1) )  // 2      )

        # Increment n
        n += 1
        
    return pentagonal_numbers_list


def find_pentagonal_pair():
    start_time = time()
    # Create a list of the first x pentagonal numbers
    pentagonal_numbers_list = find_pentagonal_numbers(2168)

    # For each item in the list
    for i in range(0, len(pentagonal_numbers_list)):

        # Check it against every other item in the list, as long as it isn't the same.
        for j in range(0, len(pentagonal_numbers_list)):
            
            # If we aren't comparing the same items
            if pentagonal_numbers_list[i] != pentagonal_numbers_list[j]:
                # print(pentagonal_numbers_list[i], pentagonal_numbers_list[j])     
                # Check if the positive solution of -b + sqrt(b^2 - 4ac) / 2a  is an integer
                """ This can happen with the formula:
                Pn = n(3n - 1) / 2
                For example:
                92 = n(3n - 1) / 2
                184 = n(3n - 1) / 2
                184 = 3n^2 - n 
                3n^2 - n - 184 = 0

                So: 3n^2 - n - (sum of the Pk and Pj     or   difference of Pk - Pj)
                """
                # Find the solutions using -b + sqrt(b^2 - 4ac) / 2a
                difference_solution = ( 1 + ( (-1)** 2 - (4 * 3 * ( (pentagonal_numbers_list[i] - pentagonal_numbers_list[j]) * 2 * -1 ))) ** 0.5 ) / (2 * 3)
                sum_solution = ( 1 + ( (-1)** 2 - (4 * 3 * ( (pentagonal_numbers_list[i] + pentagonal_numbers_list[j]) * 2 * -1 ))) ** 0.5 ) / (2 * 3)

                # If the last digit of the string is a 0, it means that the solution was an integer, so the difference and sum are both pentagonal numbers
                if str(difference_solution)[-1] == "0" and str(sum_solution)[-1] == "0":
                    end_time = time()
                    # Found the first pair, so return the difference (along with other info)
                    return pentagonal_numbers_list[i], pentagonal_numbers_list[j], pentagonal_numbers_list[i] - pentagonal_numbers_list[j], i, j, end_time - start_time

Pk, Pj, difference, i, j, time_taken = find_pentagonal_pair()
print(f"Pk: {Pk}\nPj: {Pj}\nDifference: {difference}\ni: {i}\nj: {j}\nTime taken: {time_taken}")