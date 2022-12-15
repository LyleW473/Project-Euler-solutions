from time import time
"""
- Find the value of p which has the largest number of solutions 
e.g. 

a^2 + b^2 = c^2

Find solutions where
a + b + c = p

c = p - b - a

(a)^2 + (b)^2 = (p - b - a)^2
(a)^2 + (b)^2 = (p^2 - 2pb - 2pa + 2ab + a^2 + b^2)
p^2 - 2pb - 2pa + 2ab = 0 
p^2 - 2pa = 2pb - 2ab
b(2p - 2a) = p^2 - 2pa
b = (p^2 - 2pa) / 2p - 2a

(All even numbers squared are even, all odd numbers squared are odd)

if a and b are even, c = even so p is even (even + even + even = even)

if a is odd and b is odd, c is even (because odd + odd = even), so p must be even (odd + odd + even = even)

if a is odd and b is even (vice versa), c is odd, so p must be even (even + odd + odd = even)


If b is an integer, it means that we have one solution
b = (p^2 - 2pa) / 2p - 2a
"""

possible_a_b_c = []
greatest_solutions = 0
greatest_p = 0
 
start_time = time()
for p in range(2, 1000, 2):
    number_of_solutions = 0
    for a in range(2, p):
        # Uses the equation b = (p^2 - 2pa) / 2p - 2a, if (p^2 - 2pa) % 2p - 2a == 0, it means that b is an integer and not a float
        """If (p^2 - 2pa) / 2p - 2a, it means that b is an integer. 
        e.g. One of the solutions was p = 996, a =  249, if you substitute back into the equation, you get 496008 / 1494, which is 332

        a^2 + b^2 = c^2 
        sqrt(a^2 + b^2) = c
        sqrt(249^2 + 332^2) = 415

        c = 415

        a + b + c should equal p so:

        249 + 332 + 415 = 996
        996 = 996
        """
        if ((p ** 2) - 2 * (p * a) ) % ((2 * p) - (2 * a)) == 0 :
            # Increment the number of solutions
            number_of_solutions += 1

    # If the number of solutions for this current value of p is the greatest value we have found so far
    if number_of_solutions > greatest_solutions:
        # Change the greatest solutions and record the value of p 
        greatest_solutions = number_of_solutions 
        greatest_p = p
        print(greatest_solutions, greatest_p)
    
          
print("Greatest no. of solutions: ",greatest_solutions,"p value:",greatest_p)
end_time = time()
print("Time taken :", end_time - start_time)