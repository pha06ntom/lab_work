# TODO написать функцию remove
from typing import Any


def remove(list_value: list, variable: Any) -> list:
    index = 0
    for i, value in enumerate(list_value):
        if value == variable:
            index = i

    if variable not in list_value:
        raise ValueError("Элемент не найдет")

    new_list_value = list_value[:index] + list_value[index + 1:]
    return new_list_value


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
