import re

DATA_MAX = {"red": 12, "green": 13, "blue": 14}

with open("data.csv", 'r') as f:
    data = f.read().splitlines()

lost_games = set()
power_sets = []
for game in data:
    dict_game = {"red": 0, "green": 0, "blue": 0}
    id = game.split(':')[0][5:]
    game = re.sub(r'Game\s\d+:\s', '', game)
    game = game.split('; ')
    for round_game in game:
        round_game = round_game.split(', ')
        round_game = [re.sub(r"\s", ':', cubes) for cubes in round_game]
        for part in round_game:
            part = part.split(':')
            color = part[1]
            number = int(part[0])
            if dict_game.get(color) < number:
                dict_game[color] = number
            if number <= DATA_MAX[color]:
                pass
            else:
                print("Game: " + str(id))
                lost_games.add(int(id))
    power_set = 1
    for key, value in dict_game.items():
        power_set *= value
    power_sets.append(power_set)

print("Power sets: " + str(power_sets))
print("Sum of power sets: " + str(sum(power_sets)))
