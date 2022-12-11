multiple1 = int(input("Enter multiple1 "))
originalmultiple1 = multiple1
sumofmultiple1 = 0


while multiple1 < 1000:
    sumofmultiple1 = sumofmultiple1 + multiple1
    multiple1 = multiple1 + originalmultiple1
    



print("Sum of", originalmultiple1, "=", sumofmultiple1)


multiple2 = int(input("Enter multiple2 "))
originalmultiple2 = multiple2
sumofmultiple2 = 0


while multiple2 < 1000:
    sumofmultiple2 = sumofmultiple2 + multiple2
    multiple2 = multiple2 + originalmultiple2
    


print("Sum of", originalmultiple2, "=", sumofmultiple2)


LCF = originalmultiple1 * originalmultiple2
print(LCF)
originalLCF = LCF
sumofLCF = 0
while LCF < 1000:
    sumofLCF = sumofLCF + LCF
    LCF = LCF + originalLCF

print("Sum of", originalLCF, "=", sumofLCF)

SumOfMultiples = sumofmultiple1 + sumofmultiple2 - sumofLCF
print(SumOfMultiples)