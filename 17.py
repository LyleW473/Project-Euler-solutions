single_digits = [0, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
double_digits = [0, "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
special_digits = [0, "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
hundred = "hundred"
thousand = "thousand"

test_number = "692"
test_number = "542"
test_number = "997"
test_number = "120"
test_number = "400"
test_number = "404"
test_number = "300"
# 900
# 90
# 7

# For numbers that are one hundred and above.
if len(test_number) == 3:
    test_hd = test_number[0]
    test_dd = test_number[1]
    test_sd = test_number[2]
    print(test_hd, test_dd, test_sd)


    # E.g. Five hundred and five (505)          
    if (int(test_number) % 100) != 0 and len(str(int(test_number) % 100)) == 1: # If the number is not a multiple of the hundreds and the length of the string after modding by 100 is just a single digit
        text = str(single_digits[int(test_hd)] + "hundred" + "and" + single_digits[int(test_sd)])
    
    # E.g. Five hundred (500) 
    elif int(test_number) % 100 == 0:
        text = str(single_digits[int(test_hd)]) + "hundred"

    # E.g. Six hundred and eleven (611)
    elif test_dd == "1":
        print("yes")
        text = str(single_digits[int(test_hd)] + "hundred" + "and" + special_digits[int(test_sd)])

    # E.g. One hundred and ten (110)
    elif int(test_number) % 10 == 0 and int(test_number) % 100 != 0: # If the number is a multiple of 10 and not a multiple of 100, it is e.g. 910 or 150.
        text = str(single_digits[int(test_hd)] + "hundred" + "and" + double_digits[int(test_dd)])

    # E.g. Two hundred and fifty five (255)
    else:
        text = str(single_digits[int(test_hd)] + "hundred" + "and" +  double_digits[int(test_dd)] + single_digits[int(test_dd)])

print(text)