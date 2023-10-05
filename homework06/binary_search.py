from random import randint

# Реализация бинарного поиска с использованием
# Структурной, процедурной и функциональной парадигмы

def input_arr(arr):
    if len(arr) > 1:
        left = list(arr[:len(arr) // 2])
        right = list(arr[len(arr) // 2:])
        left = input_arr(left)
        right = input_arr(right)
        return concat(left, right)
    return arr

def concat(arr_1, arr_2):
    arr_res = []
    i = 0
    j = 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            arr_res.append(arr_1[i])
            i += 1
        else:
            arr_res.append(arr_2[j])
            j += 1

    while i < len(arr_1):
        arr_res.append(arr_1[i])
        i += 1

    while j < len(arr_2):
        arr_res.append(arr_2[j])
        j += 1
    return arr_res

# Создание списка
b = []
for i in range(10):
    b.append(randint(1, 50))
print('''Исходный список:''', b)
# сортировка cписка
a = input_arr(b)
# вывод на экран
print('''Отсортированный список:''', a)
# запрос искомого числа
value = int(input('''Введите искомое число: '''))
# Находим средний элемент последовательности.
# Для этого первый и последний индексы связываем с переменными,
# а индекс среднего элемента вычисляем
mid = len(a) // 2
low = 0
high = len(a) - 1
# Значение среднего элемента сравниваем с искомым значением.
# Если они равны, поиск завершается 
while a[mid] != value and low <= high:
# Иначе поиск будет проходить в одной из половин списка,
# в зависимости от того, искомое значение больше или меньше значения среднего элемента
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

print("ID =", end=" ") 
if low > high:
    print("-1")
else:
    print(mid)
