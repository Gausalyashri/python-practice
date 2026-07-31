"""Problem: Bubble Sort
Implement the bubble sort algorithm to sort a list of numbers
in ascending order, O(n^2) time.
"""

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))
