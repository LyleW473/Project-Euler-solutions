# Create a variable which is a string of the result of (2^ 1000)
number_string = str(2 ** 1000)
print(number_string)

sum = 0
# Iterate through the digits in the string
for digit in number_string:
    # Add the digit to the sum
    sum += int(digit)

print(sum)