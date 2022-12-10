import math, time

start_time = time.time()

a = 0 
b = 0  
c = 0  
d = 0
found = False

# a < b < c

for a in range(200, 332):
    for b in range(a+1, int(1000 - a)): # b must be greater than a
        c = 1000 - a - b # c would be the remainder left after a and b have been subtracted from 1000
        if (c * c) == (a * a) + (b * b) and a + b + c == 1000: # If the number has a remainder, this means that it is not a square number
            print(a,"^2 + ",b, "^2 + ", c, "^2")
            print("The product of ", a, b, c," is ", (a * b * c))
            end_time = time.time()


print("Time taken:", end_time - start_time)
