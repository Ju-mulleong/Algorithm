def selection_sort(arr, N):
    for i in range(N-1):    # 기준위치(최솟값을 찾는 구간의 시작 인덱스), 정렬 다 하면 마지막 인덱스는 안 봐도 되니까 N-1
        min_idx = i         # 최솟값 인덱스 초기화, (구간의 맨 앞 원소를 최소로 가정)
        for j in range(i+1, N):  # 실제 최솟값인지 비교하는 위치
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # 파이썬에서 가능하니까 이렇게 한것, 다른 언어에서는 temp 변수 만들어서 이리저리 할당하는 그 방법 써야됨.


arr = [10, 25, 64, 22, 11]

selection_sort(arr, len(arr))
print(arr)