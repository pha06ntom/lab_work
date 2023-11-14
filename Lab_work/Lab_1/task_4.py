users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

total_visit = len(users)
set_users = set(users)
unique_visit = len(set_users)

dict_["Общее количество"] = total_visit
dict_["Уникальные посещения"] = unique_visit

print(dict_)
