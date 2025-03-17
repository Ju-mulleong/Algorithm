# 피벗: 제일 왼쪽 요소
def hoare_partitioning(left, right):
    pivot = arr[left]
    # pivot과 비교해서 작은 건 pivot의 왼쪽, 큰 건 pivot의 오른쪽

    i = left +1
    j = right

    while i <= j:
        # i = 큰 값을 겁색하면서 '오른쪽'으로 진행
        while i <= j and arr[i] <= pivot:
            i += 1

        # j = 작은 값을 겁색하면서 '왼쪽'으로 진행
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 위 두 개의 while문을 나왔다는 건, i에서 pivot보다 큰 값 찾고, j에서 pivot보다 작은 값 찾은것

        # SWAP
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # i와 j가 교차됨. (while i <= j 나옴)
    # pivot 위치를 확정시켜주기 (j와 바꾸기)
    arr[left], arr[j] = arr[j], arr[left]
    return j    # pivot 위치 반환



# left, right : 작업 범위
def quick_sort(left, right):
    if left < right:    # 정렬이 필요한 상태다.
        # 언제나 left는 작업 범위의 맨 왼쪽, right는 작업 범위의 맨 오른쪽

        # pivot을 기준으로 정렬시킨다.
        pivot = hoare_partitioning(left, right)
        # 왼쪽 진행
        quick_sort(left, pivot - 1)
        # 오른쪽 진행
        quick_sort(pivot +1, right)

    pass

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr)-1)
print(arr)