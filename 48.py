from time import time

start_time = time()
sum = 0
for i in range(1, 1000 + 1):
    # Add i^i to the sum
    sum += int(i ** i)

end_time = time()
print(f"Last 10 digits: {str(sum)[-10:]}\nSum: {sum}\nTime taken: {end_time - start_time}")
