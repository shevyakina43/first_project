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
def rainfall_statistics(values):
    month = ["January", "February", 
        "March", "April", "May", "June", 
        "July", "August", "September", 
        "October", "November", "December"
        ]
    rain = list(map(float, values.split()))

    total = sum(rain)

    average = total / 12 # len(rain) = 12

    max_rain = max(rain)
    min_rain = min(rain)

    max_month = months[rain.index(max_rain)]
    min_month = months[rain.index(min_rain)]

    return (total, average, (max_rain, max_month), (min_rain, min_month))

data = "22 22 24 49 72 98 101 82 51 40 36 24"

result = rainfall_statistics(data)
print(result)