def factorial(n):
    # Base case
    if n == 1:
        return n
    # Recursive step
    else:
        # E.g. 5 x factorial(4)
        return n * factorial(n-1)

# Create a string from the result
factorial_string = str(factorial(100))
print(factorial_string)

sum = 0
# Iterate through the string
for i in range(0, len(factorial_string)):
    # Add the value of the digit to the sum
    sum += int(factorial_string[i])

print(sum)