
hp = 100
money = 200
items = []

while hp > 0:
    print(f"\nЗдоровье: {hp} | Денюжка: {money} | Инвентарь: {items}")
    print("1 - Лес 2 - Тимница 3 - Магаз 4 - Выход")
    ch = input("Куда идем? ")
    
    if ch == "1":
        print("\nВ лесу вы встретили Сланяру!")
        if "меч" in items:
            print("Вы убили Сланяру мечом и выбили с него 500 рублей!")
            money += 500
        else:
            print("Сланяра пнул вас! -50 здоровья")
            hp -= 50
    
    elif ch == "2":
        if "Фанарик" in items:
            print("\nВ Темнице с фанариком вы нашли сундук с 1000 рублей!")
            money += 1000
        else:
            print("\nВ темной Темнице на вас напала чубака вы умерли")
            hp -= 100
    
    elif ch == "3":
        print("\nМагазин: 1 - Меч (200руб.) 2 - Фанарик (500руб.) 3 - Выход")
        buy = input("Что покупаем? ")
        if buy == "1" and money >= 200:
            items.append("меч")
            money -= 200
        elif buy == "2" and money >= 500:
            items.append("Фанарик")
            money -= 500
    
    elif ch == "4":
        print(f"\n Спс за игру.Ваш результат: {money} золота")
        break

if hp <= 0:
    print("\nВас прибили!.")