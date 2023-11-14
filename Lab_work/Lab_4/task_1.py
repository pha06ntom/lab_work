import random

def get_unique_list_numbers() -> list[int]:
    size_list = 15
    list_numbers = []
    for _ in range(size_list):
        number = random.randint(-10, 10)
        if number not in list_numbers:
            list_numbers.append(number)
    return list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
