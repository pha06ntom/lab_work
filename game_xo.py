PLAYER_1 = 'X'
PLAYER_2 = '0'
size_field = 0


def winner(win_combination: list, symb: str) -> bool:
    if all([x == symb for x in win_combination]):
        return True


def checking_winner(game_combination: list, check_symbol: str) -> str:
    """ Функция проверки победителя"""
    if check_symbol == PLAYER_1:
        player = 'Игрок 1'
    else:
        player = 'Игрок 2'
    list_field_lines = [game_combination[i:i + size_field] for i in range(0, len(game_combination),
                                                                          size_field)]  # Список разбивается на
    # списки с числом элементов равным размеру поля
    # Проверяем выигрышную комбинацию в строку
    for index in range(len(list_field_lines)):
        if all([x == check_symbol for x in list_field_lines[index]]):
            return player
    # Проверяем выигрышную комбинацию в столбец
    for j in range(size_field):
        list_field_lines_1 = [game_combination[i] for i in range(j, len(game_combination), size_field)]
        win_symbol = winner(list_field_lines_1, check_symbol)
        if win_symbol is True:
            return player
    # Проверяем выигрышную комбинацию по диагонали
    list_field_lines_2 = [game_combination[i] for i in range(0, len(game_combination), size_field + 1)]
    win_symbol = winner(list_field_lines_2, check_symbol)
    if win_symbol is True:
        return player
    list_field_lines_3 = [game_combination[i] for i in
                          range(size_field - 1, len(game_combination) - (size_field - 1), size_field - 1)]
    win_symbol = winner(list_field_lines_3, check_symbol)
    if win_symbol is True:
        return player


def playing_field(sequence: list):
    """Функция вывода игрового поля"""
    split_list = [sequence[k: k + size_field] for k in range(0, len(sequence),
                                                             size_field)]  # Список разбивается на списки с числом элементов равным размеру поля
    for i in split_list:
        print('-' * ((
                                 size_field * 4) + 1))  # умножается на 4 и добавляется длина числа для покрытия одной ячейки: например, | 1 |, состоящей из 5-ти символов
        for j in range(len(i)):
            print(f'| {i[j]}', end=' ')
        print('|')
    print('-' * ((size_field * 4) + 1))


def check_cell_number(current_combination: list) -> int:
    """Функция проверки корректности введенного номера ячейки"""

    while True:
        playing_field(current_combination)
        cell = input(f"Введите номер ячейки от <1 до {size_field ** 2}>: ")
        if cell == '' or cell == ' ':
            print("Введено пустое значение. Пожалуйста, введите номер ячейки в виде числа!")
            continue

        if not cell.isdigit():
            print("Введена буква. Пожалуйста, введите номер ячейки числом!")
            continue

        if int(cell) < 0 or int(cell) > size_field ** 2:
            print("Пожалуйста, введите только число из указанного диапазона!")
            continue

        if current_combination[int(cell) - 1] == PLAYER_1 or current_combination[int(cell) - 1] == PLAYER_2:
            print("Данный ход уже был сделан ранее. Введите номер свободной ячейки!")
            continue

        return int(cell)


def check_size_field() -> int:
    """ Функция проверки корректности введеного размера поля"""
    while True:
        size = input('Введите размер игрового поля (одной цифрой): ')

        if size.isalpha():
            print("Размер поля не может быть буквой. Пожалуйста, введите число!")
            continue

        if size == '':
            print("Размер поля не может быть пустым значением. Пожалуйста, введите корректное число!")
            continue

        if int(size) < 0 or int(size) == 0:
            print("Размер поля не может быть отрицательным числом или нулевым значением! Пожалуйста, введите корректные данные!")
            continue

        return int(size)


def game(numerical_sequence: list, symbol_1: str, symbol_2: str) -> str:
    count = 0
    while count < size_field ** 2:
        # playing_field(numerical_sequence)
        cell_number = check_cell_number(numerical_sequence)

        if count % 2 == 0:
            numerical_sequence[cell_number - 1] = symbol_1
            winner = checking_winner(numerical_sequence, symbol_1)
        else:
            numerical_sequence[cell_number - 1] = symbol_2
            winner = checking_winner(numerical_sequence, symbol_2)

        if winner:
            print("Победная комбинация:")
            playing_field(numerical_sequence)
            return f'Победитель: {winner}'

        count += 1

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
    numerical_sequence_field = [i + 1 for i in range(0, size_field ** 2)]  # последовательность, содержащая номера ячеек
    # поля в зависимости от размера поля
    result_string = game(numerical_sequence_field, player_symbol_1, player_symbol_2)
    print(result_string)
    print("Конец игры!")


if __name__ == "__main__":
    print("Добро пожаловать в игру 'Крестики-нолики'")
    size_field = check_size_field()
    app()
