# 12
# n = 0
# result = 1
# while n < len(numbers):
#     result *= numbers[n] # result = result * numbers[n]
#     n += 1
 
# print(result)

# 16
numbers = list(map(int, input("Enter list: ").split()))
index = 4

# while len(numbers) > index:
while numbers:
    # index %= len(numbers)  
    index2 = index % len(numbers)
    numbers.pop(index2)
    print(numbers)

