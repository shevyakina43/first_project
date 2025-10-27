# Розгалудження

# 1. Напишіть програму, в якій користувач вводить пароль і 
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


# 2. Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
# name1 = input("Enter name1: ")
# name2 = input("Enter name2: ")

# # if name1 < name2:
# #     print(name1, name2)
# # else:
# #     print(name2, name1)

# if name1 <= name2:
#     print(name2, name1)
# print(name1, name2)


# 3. Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. 
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


# 4. Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, 
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


# 5.Напишіть програму, в якій користувач вводить значення температури, і, 
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



# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. 
# Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, 
# а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. 
# Непарні номери від 19 до 28 - червоні, а парні номери - чорні. 
# Непарні номери від 29 до 36 - чорні, а парні номери - червоні. 
# Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. 
# Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.


# numer = int(input("Enter number: "))
# if number == 0:
#     print()





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




# Вводяться координати (x, y) точки A і радіус кола (r). 
# Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.
# Вхідні дані:
# 3
# 4
# 5
# -2
# 5
# 3
# Вихідні дані:
# The point belongs to the circle
# The point is outside the circle




# Дано натуральное число. Визначити, чи закінчується число парною цифрою. Якщо так, то виведе True, інакше False.




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





# Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем)
# парне або непарне. Якщо так, то виведе True, інакше False.





# Відомі рік і номер місяця народження людини, 
# а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). 
# Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.