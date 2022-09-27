'''5. Умножить два бинарных числа в формате строк
На вход подаются две строки X1 и X2, содержащие бинарные числа.
Необходимо вывести их бинарное произведение в формате строки.'''

def is_bin(num):
    try:
        num = int(num, 2)
        return num
    except ValueError:
        return -1

def multi(num1,num2):
    if is_bin(num1) < 0 or is_bin(num2) < 0:
        return "Wrong input!"

    return str(bin(int(num1,2) * int(num2,2)))
 
num1 = input("Введите 1-е число: \n")

num2 = input("Введите 2-е число: \n")

print("Результат: " + multi(num1,num2))