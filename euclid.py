'''
Алгоритм Евклида
Вычисление наибольшего общего делителя.
'''

def euclid(a, b):
    """
    Функция, вычисляющая наибольший общий делитель алгоритмом Евклида.
    Аргументы: числа, для которых вычисляется наибольший общий делитель.
    Возвращает: 
    * None, если переданы нечисловые параметры;
    * int, если все прошло успешно.
    """
    
    if not isinstance(a, int) or not isinstance(b, int):
        return None
    if a < b:
        a, b = b, a
    remainder = a % b
    gcd = b
    while remainder != 0:
        gcd = remainder
        a, b = b, remainder
        remainder = a % b
    return gcd    

num1 = input("Введите первое число: ")
if not num1.isdigit():
    print(num1, "не число!")
    exit()
    
num2 = input("Введите второе число: ")
if not num2.isdigit():
    print(num2, "не число!")
    exit()

num1 = int(num1)
num2 = int(num2)

print("Наибольший общий делитель: ", euclid(num1, num2))

# Пауза перед закрытием консоли.
input("Нажмите Enter.")
    
    