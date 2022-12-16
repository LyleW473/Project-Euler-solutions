"""
single digits 1 to 9 # 9 numbers 9 x 1 = 9
double digits 10 to 99 # 90 numbers 90 x 2 = 180        , 9 + 180 = 189
triple digits 100 to 999 # 900 numbers 900 x 3 = 2700   , 189 + 2700 = 2889th digit
four digits 1000 to 9999 # 9000 numbers 9000 x 4 = 36000  , 2889 + 36000 = 38,889
90000 x 5 = 450000              38889 + 450000 = 488,889
900000 x 6 = 5400000            488889 + 5400000 = 5,888,889

""" 

digit_count = 0
d_num = 1000000
for i in range(1, 9999999999): 
    
    digit_count += len(str(i))
    # The first digit of i will be d1, d10, d1000, d10000, d100000, d1000000
    if digit_count >= d_num:
        print(digit_count) # If digit_count = 1000005, and i = 185185 go back 5 digits, so 1. This value refers to the nth digit
        print(str(i))
        break

"""
From inputting different values for d_num i.e. 1, 10, 100, 1000, 10000, 100000, 1000000 the values are:

1 x 1 x 5 x 3 x 7 x 2 x 1 = 210
"""