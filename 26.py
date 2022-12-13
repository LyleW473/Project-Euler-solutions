def find_recurring_cycles(d):
    """ You can find the length of the recurring cycles by using MOD.

        Keep repeating the same formula, until we see a digit that we have already seen before: 
        (previous remainder * 10) % d

        1. 1 % 7 = 1

        2.  (1 * 10) % 7 = 3

        3. (3 * 10) % 7 = 2

        4. (6 * 10) % 7 = 4

        5. (4 * 10) % 7 = 5

        6. (5 * 10) % 7 = 1 [Exit the loop here]

        The length of the list of digits will be the length of the recurring cycle

    """
    list_of_digits = []
    # First calculation
    last_calculation_result = 1
    next_calculation  = last_calculation_result % d

    # WHile we haven't found the same
    while next_calculation not in list_of_digits:
        # Append the calculation to the list of digits
        list_of_digits.append(next_calculation)
        # Find the next calculation by doing: (Previous remainder) * 10 MOD d
        next_calculation = last_calculation_result * 10 % d
        # Set the last calculation result to be the result of this iteration
        last_calculation_result = next_calculation

    # Return the digits with the longest length
    return len(list_of_digits), d

longest_recurring_cycle = 0
greatest_fraction = 0
greatest_value_d = 0

# For all values of 1 <=  d < 1000
for d in range(1, 1000):
    # If the length of the recurring cycle is greater than the longest recurring cycle that we have found so far
    if find_recurring_cycles(d)[0] > longest_recurring_cycle:
        # Set the new longest recurring cycle to be the current one
        longest_recurring_cycle = find_recurring_cycles(d)[0]
        # Record the fraction and the value of d
        greatest_fraction = str(1/d)
        greatest_value_d = d

print(f" Fraction: {greatest_fraction}, Length of cycle: {longest_recurring_cycle}, d: {greatest_value_d}")