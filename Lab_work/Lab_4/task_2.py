import random
from random import choice


EAGLE = "Орел"
TAILS = "Решка"


coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    count_eagle = 0
    count_tails = 0
    for i in range(count):# TODO подсчитать количество выпаданий орлов и решек
        random_coin = choice(coin)
        if random_coin == EAGLE:
            count_eagle += 1
        else:
            count_tails += 1
    frequency = min(count_eagle,count_tails) / max(count_eagle, count_tails)
    list_freq.append(round(frequency, 3))
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
