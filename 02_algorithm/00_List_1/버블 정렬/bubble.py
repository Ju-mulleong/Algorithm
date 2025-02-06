def bubble_sort(arr):
    n = len(arr)    # 6
    for i in range(n-1, 0, -1):    # 5, 4, 3, 2, 1
        for j in range(i):  # 01234, 0123, 012, 01, 0
            if arr[i] > arr[i+1]:   # [0]과 [1] 비교.... [4] 와 [5] 비교
                arr[i], arr[i+1] = arr[i+1], arr[i]


arr = [3, 41, -5, 3, 2, 9]

print(bubble_sort(arr))
