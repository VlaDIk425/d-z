# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно
tariffs = {
    "МТС": {"МТС": 1.0, "Билайн": 1.5, "Мегафон": 2.0, "Теле2": 1.2},
    "Билайн": {"МТC": 1.5, "Билайн": 1.0, "Мегафон": 1.8, "Теле2": 1.3},
    "Мегафон": {"МТС": 2.0, "Билайн": 1.8, "Мегафон": 1.0, "Теле2": 1.4},
    "Теле2": {"МТС": 1.2, "Билайн": 1.3, "Мегафон": 1.4, "Теле2": 1.0}
}

base = float(input("Введите базовую стоимость разговора (руб.): "))

print("\nДоступные операторы:")
for operator in tariffs:
    print(f"- {operator}")

from_operator = input("\nВыберите оператора отправления: ").strip()
if from_operator not in tariffs:
        print("Ошибка: такого оператора нет!")
print("\nДоступные операторы:")
for operator in tariffs:
    print(f"- {operator}")
    to_operator = input("\nВыберите оператора назначения: ").strip()
    if to_operator not in tariffs:
        print("Ошибка: такого оператора нет!")
    try:
        tariff_multiplier = tariffs[from_operator][to_operator]
        total = base * tariff_multiplier
        print(f"\nИтоговая стоимость разговора: {total} руб.")
    except KeyError:
        print("Ошибка при расчете тарифа!")