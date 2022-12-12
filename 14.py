from time import time

def check_if_even(number):

    if number % 2 == 0:
        return True
    if number % 2 == 1:
        return False



greatest_count = [0, 0] # Count, starting_number
greatest_chain_list = []
chain_list = []

start_time = time()
for i in range(1, 1000000):

    starting_number = i
    count = 1 # Count is 1 including the starting number
    chain_list = [starting_number]

    while starting_number != 1:

        # If the starting number is even 
        if check_if_even(starting_number) == True:
            # Make n = n / 2
            starting_number = int(starting_number // 2)

        elif check_if_even(starting_number) == False:
            # Make n = 3n + 1
            starting_number = int((starting_number * 3) + 1)

        count += 1  

    
    # If the count is greater than the greatest count
    if count >= greatest_count[0]:
        #print("here", count)
        # Set the greatest count to be the 
        greatest_count[0] = count
        # Set the starting number that yields the greatest amount of terms to be the only item in the list
        greatest_count[1] = chain_list[0]


end_time = time()

print("Greatest count", greatest_count)
print("Time taken", end_time - start_time)

