from time import time 
""" 
To be considered pandigital 1 through 9, the multiplicand, multiplier and product must be 9 digits long

123456789
987654321

"""
# Limit for 2 digit multiplicand and 2 digit multiplier
print(76 * 98)
print(78 * 96)
print(87 * 96)

# Multiplicand cannot be single digit unless the multiplier is 4 digits
print(9 * 876)
print(7 * 1234)

# Limit for 2 digit multiplicand and 3 digit multiplier
print(10 * 987)

set_of_products = set()
sum = 0
start_time = time()

# Single digit multiplicand and 3 digit to 4 digit multiplier
for m1 in range(1, 9): # 

    for m2 in range(999, 9999 + 1):
        
        # If the length of the string is
        if len(str(m1)) + len(str(m2)) + len(str(m1 * m2)) == 9:
            numbers_string = str(m1) + str(m2) + str(m1 * m2)
            # If the length of the string is 9 digits long and 0 isn't one of those digits
            if len(set(numbers_string)) == 9 and "0" not in set(numbers_string):
                print(numbers_string)
                # Add the product to the set of products
                set_of_products.add(str(m1 * m2))


# Double digit multiplicand and single digit to triple digit multiplier
for m1 in range(0, 99 + 1):

    for m2 in range(0, 987 + 1):
        
        # If the length of the string is
        if len(str(m1)) + len(str(m2)) + len(str(m1 * m2)) == 9:
            numbers_string = str(m1) + str(m2) + str(m1 * m2)
            # If the length of the string is 9 digits long and 0 isn't one of those digits
            if len(set(numbers_string)) == 9 and "0" not in set(numbers_string):
                print(numbers_string)
                # Add the product to the set of products
                set_of_products.add(str(m1 * m2))

print(set_of_products)

# For all products in the set of products
for product in set_of_products:
    # Add it to the sum
    sum += int(product)

print(sum)
end_time = time()
print("Time taken:", end_time - start_time)