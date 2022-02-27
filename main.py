from random import randint
from time import time

from Heap import *
from sorting import *


def menu():
    print("Selectati o optiune:")
    print("1. Test viteza algoritmi de sortare")
    print("2. Heap Sort cu siruri de caractere")
    print("3. Quick Sort cu siruri de caractere")

    option = input()
    while option != '1' and option != '2' and option!='3':
        print("Optiune invalida!")
        option = input()

    if option == '1':
        testViteza()
    elif option == '2':
        heapSortString()
    else:
        quickSortString()


def testViteza():
    array = []
    for i in range(10000):
        array.append(randint(0, 10000))

    print("HeapSort - O(n log n): ", end="")
    array_copy = array.copy()
    start = time()
    heapSort(array_copy)
    end = time()
    print(end - start, "secunde")

    print("QuickSort - O(n log n): ", end="")
    array_copy = array.copy()
    start = time()
    quicksort(array_copy, 0, len(array_copy) - 1)
    end = time()
    print(end - start, "secunde")

    print("BubbleSort - O(n^2): ", end="")
    array_copy = array.copy()
    start = time()
    bubbleSort(array_copy)
    end = time()
    print(end - start, "secunde")

    print("InsertionSort - O(n^2): ", end="")
    array_copy = array.copy()
    start = time()
    insertionSort(array_copy)
    end = time()
    print(end - start, "secunde")

    print("SelectionSort - O(n^2): ", end="")
    array_copy = array.copy()
    start = time()
    selectionSort(array_copy)
    end = time()
    print(end - start, "secunde")


def heapSortString():
    print("Introduceti cuvinte separate prin spatiu:")
    cuvinte = input()
    lista = cuvinte.split(" ")
    heapSort(lista)
    print("Lista sortata folosind Heap Sort este:")
    print(lista)


def quickSortString():
    print("Introduceti cuvinte separate prin spatiu:")
    cuvinte = input()
    lista = cuvinte.split(" ")
    quicksort(lista, 0, len(lista) - 1)
    print("Lista sortata folosind Quick Sort este:")
    print(lista)


menu()
