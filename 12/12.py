from time import time

def generate_triangle_numbers(n):
    count = 0
    next_number = 0 
    
    # While we haven't found the nth triangle
    while count != n:
        # Next number would be the current number + the count + 2
        next_number = next_number + count + 2

        # Increment the counter
        count += 1
    
    # The next number would be pointing to the (n + 1)th term, so go back one term
    nth_number = next_number - count
    
    # Return the nth triangle number
    return nth_number

def count_divisors(triangle_number):

    count = 0
    # Start at 1, not 0
    i = 1

    # Loop until i * i is greater than triangle number, e.g. 4 x 4 is not greater.
    while i * i <= triangle_number:
        # If the triangle number is divisible by i
        if triangle_number % i == 0:
            # Increment the counter
            count += 1
            # If the triangle number is divisible by i, check if the number is the same as i (e.g. 4 x 4). If it isn't this means that it another factor has been found, e.g. 2 x 8 = 16, so add "8" to the factors
            if triangle_number // i != i:
                # Increment the counter
                count += 1
        # Increment i
        i += 1

    # Return count
    return count


start_time = time()
n = 1
# While the number of divisors of the triangle number is less than 500
while (count_divisors(generate_triangle_numbers(n))) < 500:
    # Increment n
    n = n + 1
    
print(generate_triangle_numbers(n))

end_time = time()
print(end_time - start_time)