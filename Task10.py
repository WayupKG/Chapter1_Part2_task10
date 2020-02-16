word = input()
print(word[2])
print(word[-2])
print(word[:5])
print(word[:-2])
print(word[::2])
print(word[1::2])
print(word[::-1])
print(word[::-2])
print(len(word))

# первый вариант
print(input().count(' ') + 1)

# Второй вариант
# def count_():
#     word = input("Введите слово с пробелами ")
#     print(word.count(' ') + 1)
# count_()