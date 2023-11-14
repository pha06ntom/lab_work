import random


def gaming_machine() -> int:
    size_number = 3
    random_three_figures = [random.randint(0, 9) for _ in range(size_number)]
    three_figures = [str(number) for number in random_three_figures]
    str_three_figures = ''.join(three_figures)
    return int(str_three_figures)

print(gaming_machine())
