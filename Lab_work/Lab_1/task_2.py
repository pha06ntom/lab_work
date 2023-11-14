list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count = len(list_players)  # кол-во игроков в списке
number = int(count / 2)

one_team = list_players[:number]
two_team = list_players[number:]

print(one_team)
print(two_team)