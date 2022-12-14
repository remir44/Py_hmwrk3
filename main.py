# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def odd_index_sum(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")


res = list(map(int, input("Введите числа через пробел:\n").split()))
odd_index_sum(res)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst1 = [int(a) for a in input("Введите числа через пробел: ").split()]
result = []
n = len(lst1)
for i in range(n):
    while i < len(lst1)/2 < n:
        n -= 1
        result.append(lst1[i] * lst1[n])
        i += 1
print(f"{lst1} => {result}")

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

new_lst = list(map(float, input("Введите числа через пробел: ").split()))
out_res = [round(i % 1, 2) for i in new_lst if i % 1 != 0]
print(f"{new_lst} => {round(max(out_res) - min(out_res), 3)}")

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Число в десятичной СС: '))
leftover = ''
while number > 0:
    leftover = str(number % 2) + leftover
    number = number // 2
print(leftover)

