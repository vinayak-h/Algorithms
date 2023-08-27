import subprocess
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]


print("Original list:", numbers)
bubble_sort(numbers)
print("Sorted List:",numbers)
