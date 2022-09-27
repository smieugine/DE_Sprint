'''4. Валидность скобок
Дана строка X, состоящая только из символов “{“, “}”, “[“, “]”, “(“, “)”. 
Программа должна вывести True, в том случае если все открытые скобки закрыты. 
Например: “[()]{}”, все открытые скобки закрыты закрывающимися скобками, потому вывод будет True. 
В случае же, если строка будет похожа на: “{{{}”, то вывод будет False, т.к. не все открытые скобки закрыты.'''

string = input("Введите строку:  \n")

def is_closed_brackets(strig):
    brackets = "{}[]()"

    open_bracket, closed_bracket = brackets[::2], brackets[1::2]
    buf = []
    for c in string:
        if c not in open_bracket and c not in closed_bracket:
            return "Wrong symbols!"
        elif c in open_bracket: 
            buf.append(open_bracket.index(c))
        elif c in closed_bracket:
            if buf and buf[-1] == closed_bracket.index(c):
                buf.pop()
            else:
                return False
    return (not buf)

print("Результат: " + is_closed_brackets(string))    
