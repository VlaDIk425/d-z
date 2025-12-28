from datetime import datetime

chas = datetime.now().hour

if chas >= 5 and chas < 12:
    print("Сейчас Утро")
elif chas >= 12 and chas < 18:
    print("Сейчас День")
elif chas >= 18 and chas < 23:
    print("Сейчас Вечер")
else:
    print("Сейчас Ночь")