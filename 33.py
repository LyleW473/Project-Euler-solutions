from time import time
""" 
- Convert the numerator into a string
- Convert the denominator into a string
- If the numerator and denominator have common digits, remove them. If the first version of the fraction e.g. 49/98 has the same value as 4/8, it is a curious fraction
- The numerator must always be less than the numerator
- Check if there is a curious fraction already in the list against the one we are observing.
- Calculate the product of the four fractions by: product of denominators / product of numerators
"""

def find_curious_fractions():
    curious_fractions_list = []
    start_time = time()

    while True:
        # For numerator
        for n in range(1, 99 + 1):
            # For denominator
            for d in range(n + 1, 100 + 1):
                
                # Assign the numerator and denominator
                numerator = str(n)
                denominator = str(d)

                # For each digit in the numerator
                for i in range(len(str(numerator))):
                    # For each digit in the denominator
                    for j in range(len(str(denominator))):

                        # If the fraction has common digits, and the common digits aren't in the same index position and the common digits are not "0"
                        if numerator[i] == denominator[j] and len(numerator) > 1 and i != j and numerator[i] != "0" and denominator[j] != "0":
                            # Remove common digits
                            new_numerator = numerator.replace(numerator[i], "")
                            new_denominator = denominator.replace(denominator[j], "")

                            # In the case that e.g. numbers 10 and 11, all 1s will be removed 
                            if len(new_numerator) > 0 and len(new_denominator) > 0 and int(new_numerator) > 0 and int(new_denominator) > 0:

                                # If the original value of the fraction is the same as the fraction after the common digits were removed, it is a curious fraction
                                if int(new_numerator) / int(new_denominator) == int(numerator) / int(denominator):
                                    
                                    # If we haven't found any curious fractions yet
                                    if len(curious_fractions_list) == 0:
                                        # Just add the curious fraction, along with its: numerator, denominator and value)
                                        curious_fractions_list.append( (numerator, denominator, int(numerator) / int(denominator)) )

                                    # Otherwise, we need to compare this fraction with other fractions in the list
                                    elif len(curious_fractions_list) > 0:   
                                        # Assume that the fraction does not have the same value as other fractions in the list until proven otherwise
                                        flag = True

                                        # Iterate through the curious fractions list
                                        for x in range(len(curious_fractions_list)):

                                            # Check that a fraction with the same value has already been added to the list
                                            if int(new_numerator) / int(new_denominator) == curious_fractions_list[x][2]:
                                                flag = False

                                        # If a fraction with the same value hasn't already been added to the list
                                        if flag == True:
                                            # Add the curious fraction to the list of curious fractions
                                            curious_fractions_list.append( (numerator, denominator, int(numerator) / int(denominator)) )

                                    # If the length of the list is 4
                                    if len(curious_fractions_list) == 4:

                                        # Set the products of numerators and denominators as 1
                                        product_of_numerators = 1
                                        product_of_denominators = 1 

                                        for y in range(len(curious_fractions_list)):
                                            # Multiply the numerators and denominators of the curious fractions
                                            product_of_numerators *= int(curious_fractions_list[y][0])
                                            product_of_denominators *= int(curious_fractions_list[y][1])
                                        
                                        # Return: The curious fractions list, the result of denominator / numerator, time taken
                                        end_time = time()
                                        return curious_fractions_list, product_of_denominators / product_of_numerators,  end_time - start_time

curious_fractions_list, product_of_denominators, time_taken = find_curious_fractions()
print(f"List of curious fractions: {curious_fractions_list}\nProduct of denominators: {product_of_denominators}\nTime_taken: {time_taken}")