from time import time
""" 
145 = curious number
1! + 4! + 5!    = 1 + 24 + 120 = 145

Maximum value a single digit can be is 9! = 362880

5 x 9! = 1814400
6 x 9! = 2177280
7 x 9! = 2540160
8 x 9! = 2903040
9 x 9! = 3265920

"""
def factorial(n):
    if n <= 1:
        return 1

    result = n

    while n != 1:
        n -= 1
        result *= n 

    return result

curious_list = []
final_sum = 0
start_time = time()
for i in range(3, 1814400):
    # Reset sum for all values of i
    sum = 0
    for j in range(0, len(str(i))):
        # Add the factorial of the digit to the sum
        sum += factorial(int(str(i)[j]))

    # Check if the sum of the factorial of the digits is equal to i
    if sum == i:
        curious_list.append(i)
        print(i, str(sum))
        final_sum += i

print(curious_list)
print(final_sum)
end_time = time()
print("Time taken: ", end_time - start_time)