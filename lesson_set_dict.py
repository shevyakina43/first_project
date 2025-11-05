# # 1
# def task1():
#     to_do = {
#         "today": ["read", "clear", "dog"],
#         "tomorrow": ["read", "call my mom"]
#     }
#     # print(to_do)
#     print("To do for today:")
#     for item in to_do["today"]:
#         print("-", item)
        
#     print("To do for tomorrow:")
#     for item in to_do["tomorrow"]:
#         print("-", item)
        
# # task1()


# # 2
# user_id = int(input("Your id: "))

# if user_id in users:
#     print(f"Hello, {user[user_id]}! ")
# else:
#     print("Hello, all")

# 3
# films = {'Avengers: Endgame': 2019,
#     'Guardians of the Galaxy': 2014,
#     'Iron Man': 2008,
#     'Thor': 2011}

# # sorted(films.items())
# sorted_films = dict(sorted(films.items()))

# print(films)
# print(sorted(films.items()))
# print(sorted_films)
# for name, year in sorted_films.items():
#     print(f"('{name}': {year})")

# for name in sorted_films.items():
#     print(f"('{name}')



# 4
# def task4():

# n =int(input("n: "))

# # squares = {} # dict()
# # for i in range(1, n+1):
# #     # dict[key] = value
# #     squares[i] = i ** 2

# squares = {i: i ** 2 for i in range(1, n+1)}

# print(squares)

# 5
# def task5():
#     weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# days = 

# n = 
# for name, year in week_dict.items()
#     if number == n:
#         print(day)
#         break


# # 6
# def task6():
#     text = "Lorem ipsum dolor sit amet" # создаем переменную text и сохраняем в неё строку
#     text = list(text) # превращаем строку в список символов; теперь каждый символ - отдельный элемент списка
#     letters = {i: text.count(i) for i in text}  # создаем словарь через словарные выражения (dictionary comprehension); для каждого символа i в списке text считаем, сколько раз он встречается

#     print(letters) # выволим полученный словарь, где ключ - буква, значение - количество повторений

# # 7
# def task7():
#     text = "Project Gutenberg offers over 59,000 free eBooks"

#     number_count = 0
#     alpha_count = 0

#     for ch in text:
#         if ch.isdigit():
#             number_count += 1
#         elif ch.isalpha():
#             alpha_count += 1


#     result = {"LETTERS": alpha_count, "DIGITS": number_count}

#     # print(result)
#     for key, value in result.items():
#         print(key, value)

# # 10
# def task10():
#     number1 = [1, 5, 3, 8, 0, 1]
#     number2 = [23, 9, 0, 1, 5]

#     rusult = len(set(number1 + number2))
#     print(rusult)

# number1 = {1, 5, 3, 8, 0, 1}
# number2 = {23, 9, 0, 1, 5}

# # обьединение множин
# print(number1.union(number2))
# print(number1 | number2) # a | b

# # a - b = a (без b)
# print(number1.difference(number2))
# print(number1 - number2)

# # обьединение множин - перетин
# print(number1.symmetric_difference(number2))
# print(number1 ^ number2)

# # перетин множин (общие элементы)
# print(number1.intersection_update(number2)) 
# print(number1 ^ number2)





# ✅ Задача 1
# Пользователь вводит число. Выведи его умноженное на 5.
# Пример ввода:
# 4
# Пример вывода:
# 20

# n = int(input("Enter number: ")) 
# print(n * 5)


# ✅ Задача 2
# Пользователь вводит два числа. Выведи их сумму.
# Пример ввода:
# 7
# 3
# Пример вывода:
# 10

# n1 = int(input("Enter number1: ")) 
# n2 = int(input("Enter number2: ")) 
# print(n1 + n2)


# ✅ Задача 3
# Пользователь вводит число. Выведи его последнюю цифру.
# Подсказка: последняя цифра — это число % 10
# Пример:
# 123 → 3

# n = int(input("Enter number: "))  # считала число с помощью input(), и преобразоывала его в int
# print(n % 10)


# ✅ Задача 4
# Пользователь вводит имя. Выведи приветствие в формате:
# Привет, <имя>!
# Здесь нужно просто input(), без int().

# name = input("Name: ") 
# print("Hello, " + name)


# ✅ Задача 5
# Пользователь вводит число. Выведи:
# "Число положительное", если оно > 0
# "Число отрицательное", если оно < 0
# "Ноль", если введено 0

# n = int(input("Enter number: ")) 

# name_of_number = " " 
# if n < 0: 
#     name_of_number = "Positive number"
# elif n > 0: 
#     name_of_number = "Negative number" 
# else: 
#     name_of_number = "Zero"
# print(name_of_number)