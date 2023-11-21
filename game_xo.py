import os

PLAYER_1 = 'X'
PLAYER_2 = '0'
SIZE_FIELD = 0  # TODO заменить на size_field


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def winner(win_combination: list, symb: str):
    if all([x == symb for x in win_combination]):
        return True


def checking_winner(game_combination: list, check_symbol: str) -> bool:
    """ Функция проверки победителя"""
    list_field_lines = [game_combination[i:i + SIZE_FIELD] for i in range(0, len(game_combination),
                                                                          SIZE_FIELD)]  # Список разбивается на списки с числом элементов равным размеру поля
    # Проверяем выигрышную комбинацию в строку
    for index in range(len(list_field_lines)):
        if all([x == check_symbol for x in list_field_lines[index]]):
            return True
    # Проверяем выигрышную комбинацию в столбец
    for j in range(SIZE_FIELD):
        list_field_lines_1 = [game_combination[i] for i in range(j, len(game_combination), SIZE_FIELD)]
        win_symbol = winner(list_field_lines_1, check_symbol)
        if win_symbol is True:
            return True
    # Проверяем выигрышную комбинацию по диагонали
    list_field_lines_2 = [game_combination[i] for i in range(0, len(game_combination), SIZE_FIELD + 1)]
    win_symbol = winner(list_field_lines_2, check_symbol)
    if win_symbol is True:
        return True
    list_field_lines_3 = [game_combination[i] for i in
                          range(SIZE_FIELD - 1, len(game_combination) - (SIZE_FIELD + 1), SIZE_FIELD - 1)]
    win_symbol = winner(list_field_lines_3, check_symbol)
    if win_symbol is True:
        return True


def playing_field(sequence: list):
    """Функция вывода игрового поля"""
    split_list = [sequence[k: k + SIZE_FIELD] for k in range(0, len(sequence),
                                                             SIZE_FIELD)]  # Список разбивается на списки с числом элементов равным размеру поля
    for i in split_list:
        print('-' * ((
                             SIZE_FIELD * 4) + 1))  # умножается на 4 и добавляется 1 для покрытия одной ячейки | 1 |, состоящей из 5-ти символов
        for j in range(len(i)):
            print(f'| {i[j]}', end=' ')
        print('|')
    print('-' * ((SIZE_FIELD * 4) + 1))


def check_cell_number() -> int:
    """Функция проверки корректности введенного номера ячейки"""

    while True:
        cell = input(f"Введите номер ячейки от <0 до {SIZE_FIELD ** 2}>: ")
        if not cell.isdigit():
            print("Пожалуйста, введите номер ячейки в виде числа!")
            cls()
            continue
        elif int(cell) < 0 or int(cell) > SIZE_FIELD ** 2:
            print("Пожалуйста, введите только число из указанного диапазона!")
            cls()
            continue
        else:
            break
    return int(cell)


def game(numerical_sequence: list, symbol_1: str, symbol_2: str) -> str:
    count = 0
    while count < SIZE_FIELD ** 2:
        playing_field(numerical_sequence)
        cell_number = check_cell_number()
        if count % 2 == 0:
            numerical_sequence[cell_number - 1] = symbol_1
            win = checking_winner(numerical_sequence, symbol_1)
        else:
            numerical_sequence[cell_number - 1] = symbol_2
            win = checking_winner(numerical_sequence, symbol_2)
        if win is True:
            return 'Ты победил!'
        count += 1
        cls()
    return 'Ничья!'


def checking_symbol_player() -> str:
    """ Функция ввода символа Игрока 1 и проверка на корректность введеного символа"""
    while True:
        player_symbol = input('Каким символом будет ходить Игрок 1: ').upper()
        if player_symbol == PLAYER_1 or player_symbol == PLAYER_2:
            break
        else:
            print("Пожалуйста, введите только 'X' или '0'!")
            continue
    return player_symbol


def app():
    player_symbol_1 = checking_symbol_player()
    # Определяем каким символом будет ходить игрок 2 в зависимости от введенного символа игрока 1
    if player_symbol_1 == PLAYER_1:
        player_symbol_2 = PLAYER_2
    else:
        player_symbol_2 = PLAYER_1
    numerical_sequence_field = [i + 1 for i in range(0,
                                                     SIZE_FIELD ** 2)]  # последовательность, содержащая номера ячеек
    # поля в зависимости от размера поля
    result_string = game(numerical_sequence_field, player_symbol_1, player_symbol_2)
    print(result_string)
    print("Конец игры!")


if __name__ == "__main__":
    print("Добро пожаловать в игру 'Крестики-нолики'")
    SIZE_FIELD = int(input('Введите размер игрового поля (одной цифрой): '))
    app()
