data = [5, 2, 3, 4, 1]

def bubble_sort(ls):
    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

def selection_sort(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
                ls[min_index], ls[j] = ls[j], ls[min_index]
    return ls

print(bubble_sort(data))