"""Problem: Merge Two Sorted Lists
Merge two already-sorted lists into a single sorted list,
without using the built-in sorted() function.
"""

def merge_sorted_lists(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


if __name__ == "__main__":
    print(merge_sorted_lists([1, 3, 5, 7], [2, 4, 6, 8]))
