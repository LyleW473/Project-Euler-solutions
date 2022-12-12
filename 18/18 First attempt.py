numbers = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 """

# Separating all items as individual items in a list
numbers = numbers.replace(" ", "")
numbers = numbers.replace("\n", "")
print(numbers)

numbers_list = []

for i in range(0, len(numbers), 2):
    numbers_list.append(str(numbers[i] + numbers[i + 1]))

print(numbers_list)

# Combine numbers into their own list, respective to the row they are in
print(len(numbers_list))

temp_list = []
rows_list = []
size = 1

# Iterate the same length as the numbers list
for i in range(0, len(numbers_list)):
    # Add the number to the temporary list
    temp_list.append(numbers_list[i])

    # If the length of the temporary list is equal to the size, thats one row 
    if len(temp_list) == size:
        # Add the row to the rows list
        rows_list.append(temp_list)
        # Empty the temporary list
        temp_list = []
        # Increment the size of the next list
        size += 1

print(rows_list)

# Finding the largest item in each row


path_list = [75] # Will hold the numbers selected, revealing the "path"
previous_number_index = 0 # Holds the index of where the last largest item was selected, so that we only choose the largest item between the two items below the last largest item
sum = 75 # Holds the path sum

"""
row[0]

row[0] or row[1]

if row[1] was chosen:
choose from:
row[1] or row[2] 

if row[2] was chosen:
choose from:
row[2] or row[3]

"""

# Reverse the list
rows_list = rows_list[::-1]

greatest_sum = 0


for i in range(0, 15):
    print(rows_list[0][i])

    # Add the first
    path_list = [rows_list[0][i]] 
    # Set the previous number index to be the index of the starting item
    previous_number_index = i
    
    sum = int(rows_list[0][i])

    # Iterate through each row in the rows list
    for row in rows_list:  

        # Skip the first row
        if row == rows_list[0]:
            continue

        #print("previous index", previous_number_index)

        # if the prev index is 0, it can only go to (The far left item of the row)
        if previous_number_index == 0:

            largest_item = int(row[0])

        # if the prev index is the same as the len(row), it can only go to -1 (The far right item of the current row)
        elif previous_number_index == len(row):
            largest_item = int(row[-1])

        # If we are selecting from one of the items that aren't on the edges of the triangle
        else:
            
            # Choose the largest item between the two items below the previous item
            largest_item = max(int(row[previous_number_index ]), int(row[previous_number_index - 1]))



        # Iterate through the row to find the index
        for index in range(0, len(row)):
            
            #print("here", row[index])
            # If the item in the row is the same as the largest item
            if int(row[index]) == largest_item:

                # Set the previous index to be the current index, so that in the next iteration, we will select from the 2 items below the item chosen in this iteration
                previous_number_index = index

                # Exit the loop so that it doesn't choose a duplicate value that is further down in the same row
                break


        # Add it to the path list
        path_list.append(largest_item)
        # Add it to the sum
        sum += largest_item
        
    

    print("Path list:", path_list)
    print("Sum",  sum)

    if sum > greatest_sum:
        greatest_sum = sum
        greatest_path_list = path_list
    

print(greatest_sum, greatest_path_list)

        

