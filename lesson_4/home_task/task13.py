#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(n)): #len - каждый элемент списка массива
    n[i] += 1
    print(n[i])

