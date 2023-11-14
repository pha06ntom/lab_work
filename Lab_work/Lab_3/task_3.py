# TODO  Напишите функцию count_letters


def count_letters(text):
    dict_text = {}
    COUNT = 0
    text_list = list(''.join(text.lower().split()))
    for letter in text_list:
        if letter.isalpha() is True:
            dict_text[letter] = dict_text.get(letter, COUNT) + 1
    return dict_text


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letter):
    sum_all_letter = 0
    dict_frequency = {}
    for val in dict_letter.values():
        sum_all_letter += val
    for key in dict_letter.keys():
        dict_frequency[key] = round((dict_letter[key] / sum_all_letter), 2)
    return dict_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_all_letter = count_letters(main_str)
dict_frequency_letter = calculate_frequency(dict_all_letter)

for key_letter, freq in dict_frequency_letter.items():
    print(f'{key_letter}:{freq: .2f}')
