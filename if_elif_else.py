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




