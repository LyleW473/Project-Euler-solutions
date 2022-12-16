import string
from time import time

def generate_triangle_numbers(last_num):
    triangle_num_list = [1] # t1 is already in the list
    # Uses formula: tn = (1/2)n * (n + 1) 
    # Start at t2 = 1/2(2)(2 + 1)
    n = 2
    # While the last item is less than the limit number we added
    while triangle_num_list[-1] <= last_num:
        # Add to list
        triangle_num_list.append(   int(  ( 0.5 * n ) * (n + 1)   ) ) 
        
        # Increment n
        n += 1

    return triangle_num_list

start_time = time()
# Define the alphabet in lowercase as a list
alphabet = list(string.ascii_lowercase)

#print(alphabet)

# Open the text file and set all the characters to lower-case
with open("42/words.txt", "r") as text_file:
    text_string = text_file.read().lower()

# Remove double quotation marks and convert to a list, splitting it at the commas
text_list = text_string.replace('"', "").split(",")
#print(text_list)
#print(len(text_list))

greatest_value = 0

triangle_numbers_list = generate_triangle_numbers(192)
triangle_words_list = []

# For word in text
for i in range(0, len(text_list)):
    # Reset the word value
    word_value = 0

    # For letter in word
    for j in range(0, len(text_list[i])):
        # Add the value of the letter to the new value
        word_value += alphabet.index(text_list[i][j]) + 1 # + 1 because the alphabet array is zero indexed but we need a = 1, b = 2, c = 3..

    """ Used to find the largest value a word in the text can have, so that we only generate triangle numbers below that number """
    # if word_value > greatest_value:
    #     greatest_value = word_value
    #     greatest_item = text_list[i]

    # If the word value is a triangle number, it means the word is a triangle word
    if word_value in triangle_numbers_list:
        triangle_words_list.append(text_list[i])

#print(text_list)
# The word with the graetest value is 192, so generate all triangle numbers 
# print(greatest_item, greatest_value)

print(len(triangle_words_list))
end_time = time()
print("Time taken: ", end_time - start_time)



