import re
from functools import reduce

with open('input.txt') as f:
    data = f.readlines()

data = [x.strip() for x in data]

numbers = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

data3 = []
for line in data:
    temp = ""
    for char in line:
        temp += char
        for word, digit in numbers.items():
            temp = re.sub(word, digit, temp, flags=re.IGNORECASE)
    print(temp)
    candidate = [int(s) for s in temp if s.isdigit()]
    if len(candidate) == 1:
        data3.append(candidate[0]*10 + candidate[0])
    else:
        data3.append(candidate[0]*10 + candidate[-1])
    print(data3[-1])
print(data3)

# Sum the numbers
sum_a = reduce(lambda x, y: x + y, data3)
print(sum_a)

