
with open('input.txt') as f:
    card_lst = f.read().split('\n')

card_count_lst = [1 for x in range(len(card_lst))]

for card_indx, card in enumerate(card_lst):
    winn_num_lst, guess_num_lst = [{int(y) for y in str_input.split(' ') if y} for str_input in card.split(': ')[1].split(' | ')]
    card_winning_count = len(guess_num_lst.intersection(winn_num_lst))

    for x in range(card_indx+1, card_indx + card_winning_count+1):
        card_count_lst[x] += 1 * card_count_lst[card_indx]

print(sum(card_count_lst))

