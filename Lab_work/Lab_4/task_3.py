import random


def get_random_password() -> str:
    n = 8
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    symbol = list(alphabet + alphabet.upper()) + list(range(10))
    parol_random_list = random.sample(symbol, n)
    parol_str = ''
    for i in parol_random_list:
        parol_str += str(i)
    return parol_str


print(get_random_password())
