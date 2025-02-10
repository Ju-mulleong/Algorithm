def seq_search(arr, n, key):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == key:
                return 1
    return 0


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = 3
key = 5
