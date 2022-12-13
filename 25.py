from time import time

second_last_term = 0 # Holds (n - 2) value
last_term = 1 # Holds (n - 1) value
next_term = 0 # Holds the next term of the fibonacci sequence
index_count = 0 # Counts the index we are on 

start_time = time()
# While the nth term is not 1000 digits long
while len(str(next_term)) != 1000:
    index_count += 1
    # Set the second last term to be the value of the last term
    second_last_term = last_term
    # Set the last term to be the value of the next term
    last_term = next_term
    # Set the next term of the sequence to be the sum of the last term and the second last term
    next_term = last_term + second_last_term 

print("Index = ", index_count, "Term = ", next_term)
end_time = time()
print("Time taken: ", end_time - start_time)