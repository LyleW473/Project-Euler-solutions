from time import time

def find_palindrome():
    start_time = time()
    greatest_palindrome = 0

    for i in range(1, 999):
        for j in range(1, 999):
            # Find the product of i and j
            product = str(i * j)

            # If the first half of the digits of the product are the same as the last half of the digits of the product
            if product[0 : len(product) // 2] == product[len(product) // 2:][::-1]:

                # Check if the product is greater than the greatest palindrome we have found so far
                if int(product) > greatest_palindrome:

                    # If it is, set the greatest palindrome to be this product
                    greatest_palindrome = int(product)

    end_time = time()
    # Return the greatest palindrome
    return greatest_palindrome, (end_time - start_time)


greatest_palindrome, time_taken = find_palindrome()
print(greatest_palindrome , time_taken)
