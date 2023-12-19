import re

DATA_MAX = {"red": 12, "green": 13, "blue": 14}

with open("data.csv", 'r') as f:
    data = f.read().splitlines()

lost_games = set()
for game in data:
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
            if number <= DATA_MAX[color]:
                pass
            else:
                print("Game: " + str(id))
                lost_games.add(int(id))
                break

# Sum all the elements of the set:
lost_games = 5050 - sum(lost_games)
print("Lost games: " + str(lost_games))
