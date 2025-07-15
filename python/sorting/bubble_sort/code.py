def bubble_sort(arr):
    n = len(arr)
    # Optimized Bubble Sort
    for i in range(n - 1, -1, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            # No swaps in this pass; array is already sorted
            break

    print("After Using Optimized Bubble Sort:")
    print(" ".join(map(str, arr)))


# Main part
arr = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:")
print(" ".join(map(str, arr)))

bubble_sort(arr)
