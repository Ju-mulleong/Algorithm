N = 4
arr = [[0]*N for _ in range(N)]
copied_arr = [[x for x in arr[i]] for i in range(N)]
print(arr)
print(copied_arr)
arr[1][2] = 1
print(arr)
print(copied_arr)