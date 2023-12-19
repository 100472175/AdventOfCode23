from functools import reduce


def process(data):
    time = data[0].split()[1:]
    distance = data[1].split()[1:]
    runs = []
    for i in range(len(time)):
        runs.append(0)
        working_time = int(time[i])
        working_distance = int(distance[i])
        for k in range(working_time):
            distance_traveled = k*(working_time-k)
            if distance_traveled > working_distance:
                runs[-1] += 1
    return runs

with open('input.txt') as f:
    data = f.readlines()
# Multiply all the runs together
runs = reduce(lambda x, y: x*y, process(data))
print(f"Part 1: {runs}")
# Find the smallest run with the big race
with open('input_v2.txt') as f:
    data = f.readlines()
runs = reduce(lambda x, y: x*y, process(data))
print(f"Part 2: {runs}")
