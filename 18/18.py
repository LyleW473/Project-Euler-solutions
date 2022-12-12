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


# Start from the second bottom row working up till the second row
for i in range(13, 0, -1):
    print(rows_list[i])
    print(rows_list[i + 1])

    # For each item inside of the row
    for j in range(0, len(rows_list[i])):

        # Choose the items below it and to the bottom right of it
        print(rows_list[i + 1][j], rows_list[i+1][j + 1])

        # Replace the current item with the sum of the current item with the largest item of the two items below it (bottom and bottom right)
        rows_list[i][j] = (int(rows_list[i][j]) + max(int(rows_list[i + 1][j]),int(rows_list[i+1][j + 1])))

        print(rows_list)

# The maximum path sum would be the 75 + (995 or 999) 
max_path_sum = max(int(rows_list[0][0]) + int(rows_list[1][0]), int(rows_list[0][0]) +  int(rows_list[1][1]))
print(max_path_sum)

"""
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
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23


For the first few steps
63 would be replaced by: 63 + max(4, 62) = 125
66 would be replaced by: 66 + max(62, 98) = 164
04 would be replaced by: 4 + max(98, 27) = 102


This is repeated until its just the first and second row, then find the largest path by finding the sums of whichever path i.e. 75 + 995 or 75 + 999.
75 + 999 = 1074, so the maximum path sum is 1074

"""



