import random
#Задание 1
print(eval(input("введите выражение,например:")))
#Задание 2
list1 = [random.randint(-10,10)for i in range(10)]
print(list1)
list2 = min(list1),max(list1)
negative = 0
positive = 0
zero = 0
for i in list1:
    if i < 0:
        negative += 1
    elif i > 0:
        positive += 1
    else:
        zero += 1
print(f"""
список: {list1}
мин макс элементы: {list2}
кол-во отрицательных: {negative}
кол-во положительных: {positive}
кол-во нулей: {zero}
""")
