from time import time

list1 = []
for x in range(1, 100_000):
    if x % 3 == 0:
        list1.append(x)

list2 = []
for x in range(1, 100_000):
    if x % 2 == 0:
        list2.append(x)


def intersect_slow(list1, list2):
    count = 0
    for e1 in list1:
        for e2 in list2:
            if e1 == e2:
                count += 1
    return count


def intersect_fast(list1, list2):
    count = 0
    set2 = set(list2)
    for element in list1:
        if element in set2:
            count += 1
    return count


t1 = time()  # фиксируем время начала
result = intersect_slow(list1, list2)
t2 = time()  # фиксируем время конца
print(f"Результат функции 'intersect_slow' - {result}. Время: {str(t2 - t1)} секунд")

t1 = time()  # фиксируем время начала
result = intersect_fast(list1, list2)
t2 = time()  # фиксируем время конца
print(f"Результат функции 'intersect_fast' - {result}. Время: {str(t2 - t1)} секунд")
