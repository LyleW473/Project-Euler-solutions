fib1 = 1
fib2 = 2
temp = 0
total = 2

while temp <= 4000000: # check if temp(
    temp = fib1 + fib2 # set temp as the sum of the previous 2 numbers
    fib1 = fib2 # set the 2nd previous number as the previous number before temp
    fib2 = temp # set the previos number as temp
    if temp % 2 == 0: # check if temp MOD 2 returns 0
        total = total + temp # If it is, then it is an even number so add it to total
    print(temp)

print("Total is", total)
