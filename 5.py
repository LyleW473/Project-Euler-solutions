# First (POSITIVE) number that is (EVENLY) divisible by all of the numbers from 1 to 10
MyNumber = 20
NewNumber = 0
index = 1
DivisibleByAll = False

while DivisibleByAll == False:
    while index < 11:
        NewNumber = MyNumber % index
        if NewNumber != 0: # If the remainder is not 0, this means that it is not divisible by the index
            print(MyNumber," is not divisible by ", index)
            index = 0
            MyNumber = MyNumber + 1
        else: #If the remainder is 0, this means that it is divisible by the index
            print(MyNumber," is divisible by ", index)
        index = index + 1
    if index <= 11 and NewNumber == 0:
        DivisibleByAll = True

print(MyNumber, "is the first positive number that is evenly divisible by all of the numbers from 1 to 10")
    
