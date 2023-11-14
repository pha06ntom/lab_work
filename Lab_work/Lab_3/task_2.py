# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, separator=','):
    participants_first_list = participants_first.split(separator)
    participants_second_list = participants_second.split(separator)
    set_name = set(participants_first_list).intersection(participants_second_list)
    list_name = list(set_name)
    list_name.sort()
    return list_name

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
