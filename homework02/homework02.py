# Домашнее задание - Таблица умножения
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9
# --------------------------------------------------------------------------------------
'''В данной задаче можно использовать процедурную и сруктурную парадигмы программирования, 
так как таблица умножения выводится построчно и каждое вычисление зависит от предыдущего.
В этом решении в процедурном стиле используется вложенный цикл for для перебора значений
от 1 до 10 и вывода строки с умножением на каждой итерации.
Обоснование выбора:
1. Вычисления выполняются последовательно, одно за другим. Сначала проверяется введенное число, 
затем происходит генерация и вывод таблицы умножения. 
2. структурный характер.
3. Читаемость - решение в задаче легко читаемо и понятно
'''

def check_input(n):
    if n < 1 or n > 9:
        print("Число должно быть от 1 до 9")
        return False
    return True

def print_multiplication_table(n):
    if check_input(n):
        for i in range(1, n + 1):
            for j in range(1, 10):
                print(f"{i} * {j} = {i*j}")
            print("--------------------------")    

n = int(input("Введите число n: "))
print_multiplication_table(n)