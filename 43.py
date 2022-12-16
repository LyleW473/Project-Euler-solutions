from time import time
start_time = time()

"""
Start with the last 3 digits

Find all 3 digit numbers that can be divisible by 17
289
Then attach a single digit from the remaining letters to the front of the first 2 digits of the last 3 digits, and see if it is divisible by 13
?28

Keep repeating this until the length of the number is 10, then check if all 10 digits are unique numbers (0 - 9), if it is, then it means it has the property.

"""

list_of_pandigitals = []
pandigital_sum = 0

# Lowest last 3 digits would be 012 , highest would be 987
for i in range(12, 987 + 1):

    # If the number is divisible by 17
    if i % 17 == 0:
        # Reset digits available and digits used for every value of i 
        digits_available = [0,1,2,3,4,5,6,7,8,9]
        digits_used = ""

        # For digit in i
        for j in range(0, len(str(i))):

            # Add the digit as a string to the digits used string
            digits_used += str(i)[j]

            # If the number has a duplicate value, then break
            if int(str(i)[j]) not in digits_available:
                break

            else:
                # Remove the digit from the digits available list
                digits_available.remove(int(str(i)[j]))
        
        #print(digits_available)

        letter1_list = []
        # For digits left in digits available
        for letter in digits_available:
            
            digits_available_letter_1 = digits_available.copy()

            # If a letter e.g. 7 + 28  = 728 is divisible by 13
            if int(str(letter) + str(i)[:2]) % 13 == 0:

                # Add the single digit added to the digits used
                digits_used = str(letter) + digits_used

                # Set the new number to be the letter and the first two digits of the last number
                new_num = str(letter) + str(i)[:2]

                # Remove the letter from the digits available list
                digits_available_letter_1.remove(letter)
                
                # Add the information as a list to another list
                letter1_list.append([new_num, digits_available_letter_1, digits_used])
                

        #print("letter 1 list", letter1_list)

        letter_2_list = []
        for d_number, digits_available_list, digits_used_string in letter1_list:

            for letter2 in digits_available_list:
                
                # If the number is divisible by 11
                if int(str(letter2) + d_number[:2]) % 11 == 0:

                    # Create a new used list with the letter concatenated to the front of it
                    digits_used_list_copy = str(letter2) + digits_used_string

                    # Create a copy of the digit number
                    d_number_copy = str(letter2) + d_number[:2]

                    # Create a copy of the list of digits still available, removing the letter
                    digits_available_list_copy = digits_available_list.copy()
                    digits_available_list_copy.remove(letter2)

                    # Add the information as a list to another list
                    letter_2_list.append([d_number_copy, digits_available_list_copy, digits_used_list_copy])

        #print("letter 2 list", letter_2_list)

        letter_3_list = []
        for d_number, digits_available_list, digits_used_string in letter_2_list:

            for letter3 in digits_available_list:

                # If the number is divisible by 7
                if int(str(letter3) + d_number[:2]) % 7 == 0:

                    # Create a new used list with the letter concatenated to the front of it
                    digits_used_list_copy = str(letter3) + digits_used_string

                    # Create a copy of the digit number
                    d_number_copy = str(letter3) + d_number[:2]

                    # Create a copy of the list of digits still available, removing the letter
                    digits_available_list_copy = digits_available_list.copy()
                    digits_available_list_copy.remove(letter3)

                    # Add the information as a list to another list
                    letter_3_list.append([d_number_copy, digits_available_list_copy, digits_used_list_copy])


        #print("letter 3 list", letter_3_list)    

        letter_4_list = []
        for d_number, digits_available_list, digits_used_string in letter_3_list:

            for letter4 in digits_available_list:

                # If the number is divisible by 5
                if int(str(letter4) + d_number[:2]) % 5 == 0:
                    
                    # Create a new used list with the letter concatenated to the front of it
                    digits_used_list_copy = str(letter4) + digits_used_string

                    # Create a copy of the digit number
                    d_number_copy = str(letter4) + d_number[:2]

                    # Create a copy of the list of digits still available, removing the letter
                    digits_available_list_copy = digits_available_list.copy()
                    digits_available_list_copy.remove(letter4)

                    # Add the information as a list to another list
                    letter_4_list.append([d_number_copy, digits_available_list_copy, digits_used_list_copy])
                    

        #print("letter 4 list", letter_4_list)    


        letter_5_list = []
        for d_number, digits_available_list, digits_used_string in letter_4_list:

            for letter5 in digits_available_list:

                # If the number is divisible by 3
                if int(str(letter5) + d_number[:2]) % 3 == 0:
                    
                    # Create a new used list with the letter concatenated to the front of it
                    digits_used_list_copy = str(letter5) + digits_used_string

                    # Create a copy of the digit number
                    d_number_copy = str(letter5) + d_number[:2]

                    # Create a copy of the list of digits still available, removing the letter
                    digits_available_list_copy = digits_available_list.copy()
                    digits_available_list_copy.remove(letter5)

                    # Add the information as a list to another list
                    letter_5_list.append([d_number_copy, digits_available_list_copy, digits_used_list_copy])
                    

        #print("letter 5 list", letter_5_list)    

        letter_6_list = []
        for d_number, digits_available_list, digits_used_string in letter_5_list:

            for letter6 in digits_available_list:
                # If the number is divisible by 2
                if int(str(letter6) + d_number[:2]) % 2 == 0:

                    # Create a new used list with the letter concatenated to the front of it
                    digits_used_list_copy = str(letter6) + digits_used_string

                    # Create a copy of the digit number
                    d_number_copy = str(letter6) + d_number[:2]

                    # Create a copy of the list of digits still available, removing the letter
                    digits_available_list_copy = digits_available_list.copy()
                    digits_available_list_copy.remove(letter6)

                    # Add the information as a list to another list
                    letter_6_list.append([d_number_copy, digits_available_list_copy, digits_used_list_copy])
                    

        #print("letter 6 list", letter_6_list)    


        letter_7_list = []
        for d_number, digits_available_list, digits_used_string in letter_6_list:
            
            # Note: There should only be one digit available in all of the lists, so no need to check for divisibility
            for letter7 in digits_available_list:

                # Create a new used list with the letter concatenated to the front of it
                digits_used_list_copy = str(letter7) + digits_used_string

                # Create a copy of the digit number
                d_number_copy = str(letter7) + d_number[:2]

                # Create a copy of the list of digits still available, removing the letter
                digits_available_list_copy = digits_available_list.copy()
                digits_available_list_copy.remove(letter7)

                # Add the information as a list to another list
                letter_7_list.append([d_number_copy, digits_available_list_copy, digits_used_list_copy])
            
        #print("letter 7 list (FINAL LIST)", letter_7_list)   


        for d_number, digits_available_list, digits_used_string in letter_7_list:
            # If the length of the string is 10, it means that it could include numbers from 0 to 9
            if len(set(digits_used_string)) == 10:
                flag = True
                
                # Check if all numbers 0 to 9 are in the set
                for x in range(0, 10):
                    # If one of the numbers aren't in the set, it means that it does not include numbers 0 to 9
                    if str(x) not in set(digits_used_string):
                        flag = False
                
                # If the flag is still true, this number has the sub-string divisibility property.
                if flag == True:
                    # Add it to the list, add it to the sum
                    list_of_pandigitals.append(digits_used_string)
                    pandigital_sum += int(digits_used_string)

print("Sum of numbers with the property: ", pandigital_sum)
print(list_of_pandigitals)
end_time = time()
print("Time taken: ", end_time - start_time)