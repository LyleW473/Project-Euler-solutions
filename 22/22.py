import string as alphabet_string
# Open the names file
with open("22/names.txt", "r") as names_file:
    # Make it a string
    string = str(names_file.read())

# Get rid of the commas
stripped_commas_string = string.replace(",", "")

# The starting item and last item will still have an apostrophe after splitting the string at the apostrophes, so remove those first.
stripped_commas_string = stripped_commas_string[1:-1]
# Split the string whenever there is a 
string_list = stripped_commas_string.split('""')

# Sort the list 
sorted_names_list = sorted(string_list)
print(sorted_names_list)

alphabet_list = list(alphabet_string.ascii_uppercase)
print(alphabet_list)

# Calculate the total sum of the list (and output the list with each item being its value instead of its name)
overall_sum = 0
# For names
for i in range(0, len(sorted_names_list)): # Length of the list
    sum = 0
    # For letters
    for j in range(0, len(sorted_names_list[i])): # Length of the name
        
        # Iterate through the alphabet, comparing each letter in the name with the letter in the alphabet
        for letter_index in range(0, len(alphabet_list)):
            # If the letters are the same
            if sorted_names_list[i][j] == alphabet_list[letter_index]:
                # A = 1, B = 2, not A = 0, B = 1
                sum += (letter_index + 1)
                # Exit the loop
                break

    # Add the (sum of the name times the position it is inside the list)
    overall_sum += sum * (i + 1)
    # Replace the item at this index with the sum of all the letters and the position it is in the list (OPTIONAL)
    sorted_names_list[i] = sum * (i + 1)
    

print(sorted_names_list)
print("Total sum:", overall_sum)