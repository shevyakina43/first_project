# Розгалудження

# 1. 
# Напишіть програму, в якій користувач вводить пароль і 
# якщо він співпадає із наперед визначеним паролем для цього
# користувача, то виводиться повідомлення Password accepted.. 
# y іншому випадку повідомлення буде Sorry, that is the wrong password..

# password = input("Enter password: ")
# # password = "qwerty"
# password_accept = "QwErTy"
# if password == password_accept:
#     print("Password accepted.")
# # elif password != password_accept:
# else:
#     print("Sorry, that is the wrong password..")


# 2. 
# Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
# name1 = input("Enter name1: ")
# name2 = input("Enter name2: ")

# # if name1 < name2:
# #     print(name1, name2)
# # else:
# #     print(name2, name1)

# if name1 <= name2:
#     print(name2, name1)
# print(name1, name2)


# 3. 
# Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. 
# Якщо це число або 1 або 2 або 3, то виводиться повідомлення - 
# назва числа, відповідно, One, Two, Three. B усіх інших випадках виводиться слово Unknown.

# number = int(input("Enter number: "))
# name_of_number = ""
# if number == 1:
#     name_of_number = "One"
# elif number == 2:
#     name_of_number = "Two"
# elif number == 3:
#     name_of_number = "Three"
# else:
#     name_of_number = "Unknown"
# print(name_of_number)


# 4. 
# Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, 
# яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

# letter1 = input("Enter letter1: ").lower()
# letter2 = input("Enter letter2: ").lower()

# if letter1 <= letter2:
#     print("First letter:", letter1, "Second letter:", letter2)
# else:
#     print("First letter:", letter2, "Second letter:", letter1)

# если реестр важен (заглавные или маленькие буквы)

# letter1 = input("Enter letter1: ")
# letter2 = input("Enter letter2: ")

# (letter1.lower() == letter2.lower()) and (letter1 < letter2)

# if letter1.lower() == letter2.lower():
#     if letter1 < letter2:
#         print("First letter:", letter1, "Second letter:", letter2)
#     else:
#         print("First letter:", letter2, "Second letter:", letter1)
# elif letter1.lower() < letter2.lower():
#     # if letter1 <= letter2:
#     print("First letter:", letter1, "Second letter:", letter2)
# else:
#     print("First letter:", letter2, "Second letter:", letter1)


# 5.
# Напишіть програму, в якій користувач вводить значення температури, і, 
# якщо це значення менше або дорівнює 0 градусів Цельсія, 
# необхідно вивести повідомлення A cold, isn't it?. 
# Якщо ж температура становить більше 0 і менше 10 градусів Цельсія 
# повідомлення буде Cool., у інших випадках Nice weather we're having..
# temperature = int(input("Text the temperature: "))
# if temperature <= 0:
#     print("A cold, isn't it?")
# elif temperature <= 10:
#         print("Cool.")
# else:
#     print("Nice weather we're having..")


# Middle level

# 6
# Визначте назву геометричної фігури за введеною кількістю її сторін. 
# Програма повинна підтримувати фігури від 3 до 6 сторін. 
# Якщо введена кількість сторін поза межами цього діапазону,
# програма повинна відображати відповідне повідомлення.

# print("Enter amount of sides: ")
# sides = int(input())
# if sides == int(3):
#     print ("thlangles")
# elif sides == int(4):
#     print ("rectangle")
# elif sides == int(5):
#     print ("pentagon")
# elif sides == int(6):
#     print ("hexa")
# else:
#     print("unknown")



# 7
# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. 
# Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, 
# а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. 
# Непарні номери від 19 до 28 - червоні, а парні номери - чорні. 
# Непарні номери від 29 до 36 - чорні, а парні номери - червоні. 
# Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. 
# Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.

# number = int(input("Введіть номер (0-36): "))
# if number < 0 or number > 36:
#     print("Помилка: номер повинен бути в діапазоні від 0 до 36.")
#     #print("number must be in the range from 0 to 36")
# else:
#     if number == 0:
#         color = "green"
#     elif 1 <= number <= 10:
#         if number % 2 == 0:
#             color = "black"
#         else:
#             color = "red"
#     elif 11 <= number <= 18:
#         if number % 2 == 0:
#             color = "red"
#         else:
#             color = "black"
#     elif 19 <= number <= 28:
#         if number % 2 == 0:
#             color = "black"
#         else:
#             color = "red"
#     elif  29 <= number <= 36:
#         if number % 2 == 0:
#             color = "red"
#         else:
#             color = "black"
# print(f"Номер {number} має {color} колір.")



# 8
# Дано дві точки: A(x1, y1) і B(x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.
# Вхідні дані:
# 1
# 2
# 3
# 2
# 4
# 4
# 4
# 4
# Вихідні дані:
# B
# The distance is the same

# x1 = float(input("Введіть x1: "))
# y1 = float(input("Введіть y1: "))
# x2 = float(input("Введіть x2: "))
# y2 = float(input("Введіть y2: "))

# dist_a = (x1**2 + y1**2) ** 0.5
# dist_b = (x2**2 + y2**2) ** 0.5

# if dist_a > dist_b:
#     print("a")
# elif dist_a < dist_b:
#     print("b")
# else:
#     print("The distance is the same")


# 9
# Вводяться координати (x, y) точки A і радіус кола (r). 
# Визначити, чи належить дана точка колу, 
# якщо його центр знаходиться в початку координат.
# Вхідні дані:
# 3
# 4
# 5
# -2
# 5
# 3
# Вихідні дані:
# The point belongs to the circle
# The point is outside the 

# x = float(input("Enter number: "))
# y = float(input("Enter number: "))
# r = float(input("Enter number: "))

# dist = (x**2 + y**2)**0.5  

# if dist == r:
#     print("The point belongs to the circle")
# else:
#     print("The point is outside the circle")


# 10
# Дано натуральное число. Визначити, чи закінчується число парною цифрою. Якщо так, то виведе True, інакше False.
# number = int(input("Enter number: "))

# last_digit = number % 10

# if last_digit % 2 == 0:
#     print(True)

# else:
#     print(False)


# 11
# Напишіть програму для знаходження коренів квадратного рівняння a*x² + b*x + c = 0. 
# Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено 
# три пари вхідних значень коефіцієнтів, а у вихідних даних - 
# відповідні повідомлення про кількість коренів або їх відсутність.
# Вхідні дані:
# 8
# 4
# 2
# 3.6
# 10
# -3
# 2
# 4
# 2
# Вихідні дані:
# No roots.
# 0.27 and -3.05
# -1.00





# 12
# Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем)
# парне або непарне. Якщо так, то виведе True, інакше False.





# 13
# Відомі рік і номер місяця народження людини, 
# а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). 
# Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.

# 14
# Дано чотирицифрове число. 
# Замінити усі парні цифри числа на символ * 
# і вивести число.
# Вхідні дані:

# 2358
# 2227
# 1353
# Вихідні дані:

# *35*
# ***7
# 1353

# n = input()
# result = ""
# for digit in n:
#     if int(digit) % 2 == 0:
#         result += "*"
#     else:
#         result += digit

# print(result)


