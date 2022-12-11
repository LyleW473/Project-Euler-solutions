sum = 0
list = []

for i in range(0, 1000):
    # If the number is divisible by 3,  OR, the number is divisible by 5, add the number to the sum.
    # Note: This ignores all values of i which are divisible by 15.
    if (i % 3) == 0 or (i % 5) == 0:
        print(i)
        sum += i

print(sum)