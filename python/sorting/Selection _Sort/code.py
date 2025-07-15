def selection_sort(arr):
    n = len(arr)
    # Selection sort algorithm
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

    print("After selection sort:")
    print(" ".join(map(str, arr)))


# Main part
arr = [13, 46, 24, 52, 20, 9]
print("Before selection sort:")
print(" ".join(map(str, arr)))

selection_sort(arr)
