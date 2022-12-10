square = 1
SumOfSquares = 0
while square < 101:
    SumOfSquares = SumOfSquares + (square * square)
    square = square + 1
#print(SumOfSquares)


x = 1
TotalX = 0
while x < 101:
    TotalX = TotalX + x
    x = x + 1
SquareOfSum = (TotalX * TotalX)
#print(x)
#print(TotalX)
#print(SquareOfSum)

Difference = SquareOfSum - SumOfSquares
print(Difference)
