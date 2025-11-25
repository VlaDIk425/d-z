import random
import string

def generate_parole(length = 10, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Ошибка: Не выбран тип символов."
    
    parol = ''.join(random.choice(characters) for _ in range(length))
    return parol


def check_password_strength(parol):
    score = 0
    
    if len(parol) >= 10:
        score += 2
    elif len(parol) >= 8:
        score += 1
    
    has_upper = any(c.isupper() for c in parol)
    has_lower = any(c.islower() for c in parol)
    has_digit = any(c.isdigit() for c in parol)
    has_special = any(not c.isalnum() for c in parol)
    
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    
    if char_types >= 4:
        score += 3
    elif char_types >= 3:
        score += 2
    elif char_types >= 2:
        score += 1
    
    if score >= 5:
        strength = "Сложный"
    elif score >= 3:
        strength = "Средний"
    else:
        strength = "Простой"
    
    return f"{strength} (Очки: {score})"

parol_strong = generate_parole(length=14, use_special=True)
parol_simple = generate_parole(length=6, use_upper=False, use_digits=False, use_special=False)

print(f"Сильный пароль: {parol_strong}")
print(f"Простой пароль: {parol_simple}")
print(f"Проверка сложного: {check_password_strength(parol_strong)}")
print(f"Проверка среднего: {check_password_strength('Pa$$w0rd')}")
print(f"Проверка легкого: {check_password_strength(parol_simple)}")