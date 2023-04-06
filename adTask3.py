"""Определить, позицию второго вхождения строки в списке либо сообщить, 
что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1"""

def index_2(str_list, word):
    count = 0
    for key, item in enumerate(str_list):
        if item == word:
            count += 1
            if count == 2:
                return key
    return("-1")

str_list = input().split(", ")
print(*str_list)
s = input("Что ищем ?  ")    
print(index_2(str_list,s))