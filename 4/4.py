number1 = 999
number2 = 999

list = []
list2 = []

# Check if a palindrome has been found
PalindromeFound = False
NumberOneTurn = True
while number1 != 99 and PalindromeFound == False: # While number 1 is a three digit number and palindrome has not been found
    while number2 > 900 and PalindromeFound == False: # While number 2 is greater than 900 and palindrome has not been found
        product = (number1 * number2)   
    # Check if product is a palindrome
        list = []
        list2 = []

        for i in str(product):
            list.append(i)

        # Count number of items in the string
        num_of_items = len(list)

        # Check if number has an even number of items
        if num_of_items % 2 == 0:
            # Separate the string into 2 parts
            item1 = list[:num_of_items // 2]
            item2 = list[num_of_items // 2:]

            list2.append(item1) 
            list2.append(item2)

            # Check if the first part is the same as reversed second part
            if item1 == item2[::-1]:
                # If it is, print that it is a palindrome
                print(product,"is a palindrome")
                PalindromeFound = True
            else:# If it isn't, print that it is not a palindrome
                print(product,"is not a palindrome")
                
        else: #If number has an odd number of items
            # Items 1 to middle item
            item1 = list[:(num_of_items - 1) // 2]
            # Middle item
            item2 = list[(num_of_items) // 2]
            # Items after middle item to the end of list
            item3 = list[(num_of_items + 1) // 2:]
            
            # Add items to list2
            list2.append(item1)
            list2.append(item2)
            list2.append(item3)

            # Check if the first part is the same as reversed second part
            if item1 == item3[::-1]:
                # If it is, print that it is a palindrome
                print(product,"is a palindrome")
                PalindromeFound = True
            else:# If it isn't, print that it is not a palindrome
                print(product,"is not a palindrome")
        
        number2 = number2 - 1 # Decrement number 2 until number 2 is equal to 900
    number2 = 999 # Once number 2 is equal to 900, reset it to 999
    number1 = number1 - 1 # Then decrement number 1




        

