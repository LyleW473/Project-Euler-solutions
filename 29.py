from time import time
"""
- a^b
- Use a set to get rid of any repeats
"""

start_time = time()
numbers_set = set()

# 2 <= a <= 100
for a in range(2, 100 + 1):
    # 2 <= b <= 100
    for b in range(2, 100 + 1):
        # Add the result of a^b to the set
        numbers_set.add(int(a**b))

print(numbers_set)
print("No of. distinct terms:", len(numbers_set))
end_time = time()
print("Time taken: ", end_time - start_time)