
# Стоимость тарифа - руб/км
GREEN_TARIFF = 100
YELLOW_TARIFF = 200
RED_TARIFF = 300

# Маршрут поездки и расстояния (в км) между начальным и конечным пунктом маршрута
route_trip = [
    {"route": ["дом", "работа"], "distance": 3},
    {"route": ["дом", "магазин"], "distance": 1},
    {"route": ["дом", "спортзал"], "distance": 2},
    {"route": ["работа", "спортзал"], "distance": 1.2},
    {"route": ["спортзал", "магазин"], "distance": 2},
    {"route": ["работа", "магазин"], "distance": 1.5}
]


def taxi(a: str, b: str, time_: tuple = (12, 0)) -> int:
    """Функция производит рассчет стоимости поездки на такси в зависимости от тарифа.
    Тариф определяется исходя из времени, когда совершается поездка."""

    distance_trip, price_tariff = 0, 0    # Переменные значений расстояния маршрута и тарифной ставки
    list_trip = [a.lower(), b.lower()]
    list_trip.sort()
    time_day = time_[0] + round(time_[1] / 60, 2)    # Время (в часах) начала поездки, для определения тарифа

    # Проверка корректности данных времени
    for t in time_:
        if t < 0:
            raise ValueError("Время должно быть положительным.")

    for route in route_trip:    # Определение расстояния
        route["route"].sort()
        if route["route"] == list_trip:
            distance_trip = route["distance"]
    # Если указанный маршрут не был найден в списке (значение расстояния осталось равно 0), то вызывается ошибка
    if distance_trip == 0:
        raise AssertionError('Указанный маршрут не найден')
    # Определение тарифной ставки
    if 0 <= time_day <= 8:
        price_tariff = GREEN_TARIFF
    elif 8 < time_day <= 10 or 17 <= time_day <= 21:
        price_tariff = RED_TARIFF
    else:
        price_tariff = YELLOW_TARIFF

    price_trip = distance_trip * price_tariff    # Расчет полной стоимости поездки
    return int(price_trip)


if __name__ == "__main__":
    start = 'Дом'
    end = 'Магазин'
    time_start = (2, 15)
    taxi_rade = taxi(start, end, time_start)
    print(f'Стоимость поездки по маршруту "{start.lower()}-{end.lower()}" составляет {taxi_rade} рублей')
