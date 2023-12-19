import pprint

with open('input.txt') as f:
    lines = f.read()

map_size = (len(lines.splitlines()), len(lines.splitlines()[0]))
map_data = {}
for x, line in enumerate(lines.splitlines()):
    for y, char in enumerate(line):
        map_data[(x, y)] = char


def find_adyacents(row, col):
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1)]
    return [(r, c) for r, c in neighbors if 0 <= r < map_size[0] and 0 <= c < map_size[1]]

num_set = set()
for x in range(map_size[0]):
    for y in range(map_size[1]):
        if map_data[x, y] not in "0123456789.":
            adyacents = find_adyacents(x, y)
            print("Adyacents of", x, y, "are", adyacents)
            for key in adyacents:
                string = ""
                elem = map_data.get(key)
                if elem.isdigit():
                    string = elem
                    i = key[1] - 1
                    while i >= 0 and map_data.get((key[0], i)).isdigit():
                        string = map_data.get((key[0], i)) + string
                        i -= 1

                    # Buscar hacia la derecha desde la posición dada
                    j = key[1] + 1
                    while j < map_size[1] and map_data.get((j, key[1])).isdigit():
                        string += map_data.get((j, key[1]))
                        j += 1
                    if len(string) < 2:
                        continue
                    else:
                        num_set.add(int(string))
print(num_set)
print(sum(num_set))