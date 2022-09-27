'''3. Перевод арабского числа в римское
Дано целое положительное число X, необходимо вывести вариант этого числа в римской системе счисления в формате строки. '''

def get_roman(num):
    
    if num < 1 or num > 2000:
    	return "wrong input!"

    res = ''

    num_arr = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
    sym_arr = ("I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M")
    
    i = len(num_arr) - 1
      
    while num:
        div = num // num_arr[i]
        num %= num_arr[i]
  
        while div:
            res += sym_arr[i]
            div -= 1
        i -= 1
    
    return res        
  
num = input("Введите число: \n")

print("Результат: " + get_roman(int(num)))