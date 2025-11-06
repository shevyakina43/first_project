#  1
# def name(name):
#     print(f"Hello, {name}!")
# name("Hanna")

# def name_hello(name="NON"):
#     return f"Hello, {name}!"

# print(name_hello())
# print(name_hello(name))

# 2
# def copy_string(text, n):
#     return(" " + text + " ") * n

# text = input("Enter text: ")
# n = int(input("Enter n: "))
# print(copy_string(text, n), end=" ")

# 3
# def sum_a_b(a, b):
#     return a + b

# num_1 = int(input("Num_1: "))
# num_2 = int(input("Num_2: "))

# print(sum_a_b(num_1, num_2))

# 4
# def n_letter(word, n):
#     if len(word) < n:
#         return  word
#     else:
#         return word[:n]
# print(n_letter("letter", 3))

# 5
# def find_max(a, b, c):
#     return max(a, b, c)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# largest_number = find_max(a, b, c)
# print(f"Найбільше число: {largest_number}")


# 6
# def teg_html(teg, text):
#     return f"<{teg}>{text}</{teg}>"

# text = input("Enter text: ")
# # 1 metod
# teg, string = text.split()
# # 2 metod
# teg = text.split()[0]
# string = " ".join(text.split()[1:])

# print(teg_html(teg, string))


# 10
# def rainfall_statistics(values):
#     month = ["January", "February", 
#         "March", "April", "May", "June", 
#         "July", "August", "September", 
#         "October", "November", "December"
#         ]
#     rain = list(map(float, values.split()))

#     total = sum(rain)

#     average = total / 12 # len(rain) = 12

#     max_rain = max(rain)
#     min_rain = min(rain)

#     max_month = months[rain.index(max_rain)]
#     min_month = months[rain.index(min_rain)]

#     return (total, average, (max_rain, max_month), (min_rain, min_month))

# data = "22 22 24 49 72 98 101 82 51 40 36 24"

# result = rainfall_statistics(data)
# print(result)



# 12

# def countdown(n):
#     if  n == 0:
#         print("Start!")
#     else:
#         print(n)
#         countdown(n - 1) # n -= 1 coutndown(n)
# countdown(5)

# def countdown_new(n):
#     if n > 0:
#         print(n)
#         countdown_new(n - 1)  # n -= 1 countdown(n)
#     print("Start!")

# countdown_new(5)


# ''''''
# countdown_new(5): print(5) -> countdown_new(4), print("Start!")
# countdown_new(4): print(4) -> countdown_new(3), print("Start!")
# # countdown_new(3): print(3) -> countdown_new(2), print("Start!")
# # countdown_new(2): print(2) -> countdown_new(1), print("Start!")
# # countdown_new(1): print(1) -> countdown_new(0), print("Start!")
# # countdown_new(0): print("Start!")
# # ''''''

# # print(5) -> print(4) -> print(3) -> print(2) -> pcountdown_new(1), print("Start!"), print("Start!"), print("Start!"), print("Start!"), print("Start!")
# # #print("-------------")
# # def countdown_new(2):
# #     if n > 0:
# #         print(n)
# #         countdown_new2(n - 1)  #n -= 1 countdown(n)
# # print("Start!")

# # countdown_new2(5):

# # print("-------------")
# # def countdown_new_r(n):
# #     if n > 0:
# #         print(n)
# #         countdown_new_r(n - 1) # n -= 1 countdown(n)
# #     return "Start!"
# # # print(countdown_new_r(5))



# # ! - ФАКТОРИАЛ
# def facrorial(n):
#     if n == 1:
#         return 1
#     return n * facrorial(n - 1)


# '''''
# facrorial(5): 5 * facrorial(4)
# facrorial(4): 4 * facrorial(3)
# facrorial(3): 3 * facrorial(2)
# facrorial(2): 2 * facrorial(1)
# facrorial(1): 1
# '''

# ''''''
# 5 * facrorial(4)
# 5 * 4 * facrorial(3)
# 5 * 4 * 3 * facrorial(2)
# 5 * 4 * 3 * 2 * facrorial(1)
# 5 * 4 * 3 * 2 * 1
# ''''''

# # ------------------
# def sum_numbers(a, b):
#     return a + b

# def sqr(a, b):
#     return sum_numbers(a, b) ** 2

# print(sqr(2, 7))

# #----------
# # a = 5, b = 4
# # 5 + 4
# # 5 + 1 + 4 - 1= 6 + 3
# # 7 + 2
# # 8 + 1
# # 9 + 0
# def add_number(a, b):
#     if b == 0:
#         return a
#     return helper(a + 1, b - 1)

# def helper(a, b):
#     if b == 0:
#         return a
#     return add_number(a + 1, b - 1)

# print(add_number(5, 4))
