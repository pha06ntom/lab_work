# TODO Напишите функцию для поиска индекса товара
def search(list_product: list, product: str):
    for index, current_product in enumerate(list_product):
        if current_product == product:
            return index

items_list = ('яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан')

for find_item in ['банан', 'груша', 'персик']:
    index_item = search(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
