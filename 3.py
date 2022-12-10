# Finds all the factors of said number
Factors = []
LPM = True
number = 1

while LPM and number != 13195:
    print(number)
    if 13195 % number == 0: # if 13195 MOD number = 0
        # Then it is divisible by that number
        Factors.append(number)
        # Increase the number to find next largest factors
    number = number + 1
    
print(Factors)

PrimeFactors = []

# Finds all the prime factors inside the factors list
for i in Factors:
    number2 = 1
    count = 0
    while number2 <= i :
        print(number2)
        if (i % number2) != 0: # if the remainder is anything but 0, this means that it is not divisible by number2
            pass
        else: # If it does then it means it is divisble by number2
            count = count + 1 #so increment count
        number2 = number2 + 1 # increment number2 
            
    if count <= 2: # A prime factor should only have 2 factors, so if it is less than or equal to 2, add it to the prime factors list
        PrimeFactors.append(i)
            
print(PrimeFactors)


# count how many times 1 is divisible by all the numbers before it, if count is greater than 2, it is not prime

        

