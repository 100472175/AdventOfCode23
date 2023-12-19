from functools import reduce

with open('input.txt') as f:
    data = f.readlines()

data = [x.strip() for x in data]
# Get only the numbers in the strings
print(data)
data2 = []
data = [p for p in data]
for line in data:
    # Get only the numbers of the strings
    data2.append([int(s) for s in line if s.isdigit()])

# Retain only the first and last numbers
data3 = []
for line in data2:
    data3.append(line[0]*10 + line[-1])
print(data3)

# Sum the numbers
sum_a = reduce(lambda x, y: x + y, data3)
print(sum_a)