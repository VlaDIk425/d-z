#Задача 1
def display_quote():  
    quote = "Don't let the noise of others' opinions drown out your own inner voice."  
    print("\n" + "*" * 50)  
    print(" " * 1 + quote)  
    print("*" * 50 + "\n")  
#Задача 2
def print_numbers(start, end):
    if start > end:
        start, end = end, start
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)
print_numbers(2, 10) 
#Задача 3-_-
#Задача 4

def draw_line(length, direction, symbol):  

    if direction == 'horizontal':  
        return symbol * length  
    elif direction == 'vertical':  
        return '\n'.join([symbol for _ in range(length)])  
    else:  
        raise ValueError("Направление должно быть 'horizontal' или 'vertical'")  
  

print(draw_line(5, 'horizontal', '*'))  
print(draw_line(3, 'vertical', '+'))    

# Задание 5

def diapozon_num(start, end):
    return sum(range(start, end + 1))  
print(diapozon_num(1,3))
#Задача 6

def true_folse(num):
    if num <= 1:  
        return False  
    if num == 2:  
        return True  
    if num % 2 == 0:  
        return False  
    for i in range(3, int(num ** 0.5) + 1, 2):  
        if num % i == 0:  
            return False  
      
    return True 

#Задача 7 -_-





