#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)
# Пример:

import math
mass = int(input("Введите единицу массы тела: "))
M = int(input("Введите массу тела: ")) # Введите единицу массы тела
# kg = 1 #       1 - килограмм
# mg = 2 #       2 — миллиграмм
# gr = 3 #       3 — грамм
# t = 4 #       4 — тонна
# c = 5 #       5 — центнер
def to_kilo (mass, M):
    if mass == 1:
        return M
    elif mass == 2:
        return M / 10 ** 6
    elif mass == 3:
        return M / 1000
    elif mass == 4:
        return M * 1000
    elif mass == 5:
        return M * 100
    else:
        return "Число вне допустимого диапазона"
result = to_kilo(mass, M)
print("Масса в килограммах:", result)


#Введите  массу тела

# Ответ: 1000 кг

