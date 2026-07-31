"""Problem: Binary Search
Given a sorted list and a target value, return the index of the
target using binary search, or -1 if not found. O(log n) time.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(data, 7))   # 3
    print(binary_search(data, 4))   # -1
