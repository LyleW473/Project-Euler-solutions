"""
- Uses combinatorics to find the solution
- 9! = 362880 ways, so the first 362880 permutations start with 0
- 362880 - 725760 start with 1
- 725760 - 1088640 start with 2
- The 1,000,000th permutation must start with a 2
"""

count = 0
strings_list = []

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

remaining_numbers = [2, 0, 1, 3, 4, 5, 6, 7, 8, 9]
digit_indexes = []
millionth_number = []

# The first digit must be 2
last_digit_index = 0 # So the index must be 0
ways_left = 274239 # The ways left after the first index would be int((999999) - (2 * 9!))
digit_indexes.append(last_digit_index) # Append it to the digit indexes list

for i in range(8, 0, -1):
    # E.g. int(999999 / 9!) = 2
    last_digit_index = int(ways_left / factorial(i)) 
    # E.g. 999999 / (2 * 9!) = 274239 ways
    ways_left = ways_left - (last_digit_index * factorial(i))
    # Append the digit to the digit indexes
    digit_indexes.append(last_digit_index)

    print(last_digit_index)

print("Digit indexes:", digit_indexes)
print("Remaining numbers:", remaining_numbers)

# For each digit_indexes index in digits, append the remaining number at the digit index to the millionth number
for digit_index in digit_indexes:
    # Add the number in the remaining numbers at the digit index to the millionth number
    millionth_number.append(remaining_numbers[digit_index])
    # Pop the item at this digit index
    remaining_numbers.pop(digit_index)

# Add the final number
millionth_number.append(remaining_numbers[0])
print(millionth_number)