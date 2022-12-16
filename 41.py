from time import time
"""
987654321 is the largest 9 digit pandigital

1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15
1 + 2 + 3 + 4 + 5 + 6 = 21
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45

- If the sum of digits are divisible by 3, then the number is divisible by 3.
4 digit number not divisible by 3
7 digit number not divisible by 3
So the largest prime number will be within the 4 to 7 digit range.
""" 

def is_prime(n):
    # If n is less than or equal to 1, it is not prime
    if n <= 1:
        return False
    # If n is 2, it is prime
    if n == 2:
        return True
    # If n is even, it is not prime (2 is the only even prime number)
    if n % 2 == 0:
        return False
    # Only look for odd numbers
    for i in range(3, int(n** 0.5) + 1, 2): # Increment by 2 each time as every prime number past 2 is odd.
        # If n is divisible by i
        if n % i == 0:
            return False
    # Else
    return True

start_time = time()
flag = True
# Start from the highest 7 digit number to the highest 4 digit number
for i in range(7654321 , 4321, -2): # All prime numbers past 2 are odd, so decrement by 2
    
    # If the number is a prime number
    if is_prime(i):
        # Check all the numbers from 1 to (the highest digit of that number)
        for j in range(1, len(str(i)) + 1):
            # If the number is not inside i
            if str(j) not in set(str(i)):
                # Set the flag to False
                flag = False

        # If the flag is still True, it means that it is a palindrome, and is a prime number
        if flag == True:
            print(i)
            break
        # Else reset the flag to True
        flag = True

    
end_time = time()
print("Time taken: ", end_time - start_time)