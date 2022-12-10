import time

start_time = time.time()
print("Script started")

def SumOfPrimes(n):
    sum = 0
    sieve = [True] * n
    
    
    for p in range(2, n): # Check for prime from numbers 2 to input number
        if sieve[p]: # Check if item p inside the array sieve is set to true.
            sum += p # If we find a prime number, add it to the sum of primes
            for i in range(p*p, n, p): # range(start, end, step) # When we have found a prime, for all multiples of p, we want to mark them as composite, i.e. False, as they are not prime. 
                sieve[i] = False
    return sum # Once all numbers from 2 to input number have been checked, return the total sum of all n primes.




print(SumOfPrimes(2000000))

end_time = time.time()

print("Time taken: ", end_time - start_time)
          
    
    
