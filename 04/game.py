import re

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Winner: 41 48 83 86 17
User:  83 86  6 31 17  9 48 53
"""

with open('input.txt') as f:
    lines = f.readlines()

partidas = []
for line in lines:
    cards = line.split('\n')[0].split(' | ')
    cards[0] = cards[0].split(': ')[1]
    cards[0] = re.sub(r'\s\s', ' 0', cards[0]).split(' ')
    cards[1] = re.sub(r'\s\s', ' 0', cards[1]).split(' ')
    if cards[0][0] == '':
        cards[0].pop(0)
        cards[0][0] = '0'+cards[0][0]
    if cards[1][0] == '':
        cards[1].pop(0)
        cards[1][0] = '0'+cards[1][0]
    print(cards)

    coincidencias = []
    for winer in cards[0]:
        if winer in cards[1]:
            coincidencias.append(winer)
    if len(coincidencias) == 0:
        puntuacion = 0
    else:
        puntuacion = 2**(len(coincidencias)-1)
    partidas.append(puntuacion)
print(partidas)
print(sum(partidas))

