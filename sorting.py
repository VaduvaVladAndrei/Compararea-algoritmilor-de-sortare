def bubbleSort(array):
    for i in range(len(array), 1, -1):
        for j in range(i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array


def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j - 1] and j != 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def selectionSort(array):
    for i in range(len(array) - 1):
        k = i
        for j in range(i + 1, len(array)):
            if array[k] > array[j]:
                k = j
        if k != i:
            aux = array[i]
            array[i] = array[k]
            array[k] = aux
    return array


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q)
        quicksort(array, q + 1, r)


def partition(array, p, r):
    x = array[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            if array[j] <= x:
                break
        while True:
            i += 1
            if array[i] >= x:
                break
        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j
