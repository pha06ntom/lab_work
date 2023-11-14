money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
budget = money_capital + salary

while spend < budget:
    month += 1
    income = salary - spend
    budget += income
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
