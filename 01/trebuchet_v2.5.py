import re
from functools import reduce
import time
start = time.time()
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
# Invert the dictionary
numbers_inv = {v: k for k, v in numbers.items()}


def get_number(item: str):
    if item.isdigit():
        return str(item)
    else:
        return numbers.get(item)


data2 = []
for line in data:
    data2.append([])
    # print(line)
    number_first = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    for item in number_first:
        num = get_number(item)
        data2[-1].append(num)
        # print(item[1:])
        line = re.sub(item, item[1:], line, 1, flags=re.IGNORECASE)
        # print(line)
        break
    invert_line = line[::-1]
    temp = ""
    no_llega = False
    for char in invert_line:
        temp = char + temp
        for word, digit in numbers.items():
            temp = re.sub(word, digit, temp, flags=re.IGNORECASE)
        candidate = [int(s) for s in temp if s.isdigit()]
        if len(candidate) == 1:
            data2[-1] = int(data2[-1][0]) * 10 + candidate[0]
            no_llega = True
            break

    if not no_llega:
        data2[-1] = int(data2[-1][0]) * 10 + int(data2[-1][0])


# Sum the numbers
sum_a = reduce(lambda x, y: x + y, data2)
print(sum_a)
print("Time: ", time.time() - start)