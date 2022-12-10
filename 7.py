# Identify what numbers are prime
# Have a counter for whenever a prime number is found
# When the counter is 10000, exit the loop and print the prime number
PrimeNumberCounter = 0
DivisibleByCounter = 0
MyNumber = 0
y = 1 # Dividing number


PrimeNumbers = []

while MyNumber <= 1000000000 and PrimeNumberCounter != 1000: # While we haven't checked the first 100 numbers
        while (MyNumber >= y) and DivisibleByCounter <= 2: # While MyNumber is greater than y and divisible counter is less than or equal to 2
            if (MyNumber % y) == 0: # Check if the remainder is 0, which means it is divisible by y
                DivisibleByCounter = DivisibleByCounter + 1 # Increment the divisible counter
            y = y + 1
        # When either y becomes greater than the number its checking, or its discovered that MyNumber is not prime
        # Check what the Divisible counter is
        print(DivisibleByCounter)
        if DivisibleByCounter == 2: # This is in the case that MyNumber is prime
            print(MyNumber," is a prime number")
            PrimeNumbers.append(MyNumber)
            PrimeNumberCounter = PrimeNumberCounter + 1
        else:
            print(MyNumber," is not a prime number")
        
        # Increment MyNumber
        MyNumber = MyNumber + 1
        # Reset y
        y = 1
        # Reset DivisibleByCounter
        DivisibleByCounter = 0
        



            
print(MyNumber - 1,"is the", PrimeNumberCounter,"th prime number")

            


    
