def binary_search(a, n, key):
    start = 0   # 검색 구간 설정
    end = n-1
    while start <= end:     # 검색 구간에 1개 이상의 원소가 있으면 검색, start와 end가 cross되기 전까지
        middle = (start + end) // 2     # 기준 위치 계산

        if a[middle] == key:    # 검색 성공!
            return middle

        if a[middle] > key:     # key가 middle의 왼쪽 구간에 있으면, 끝 index를 middle-1로
            end = middle - 1

        if a[middle] < key:     # key가 middle의 오른쪽 구간에 있으면, 시작 index를 middle +1로
            start = middle + 1

    return -1   # 검색 실패..


arr = [2, 4, 7, 9, 11, 19, 23]  # 이건 오름차순으로 정렬되있는 arr
print(binary_search(arr, len(arr), 7))
print(binary_search(arr, len(arr), 10))


arr2 = [9, 2, 4, 7, 23, 11, 19]     # 정렬 되있지 않은 arr2
print(binary_search(sorted(arr), len(arr), 7))
# sorted()로 정렬된 list로 하여 반환.
# 아니면, arr2 = arr2.sort()로 새롭게 정렬시킨 뒤 arr을 인수로 줘도 됨.
# .sort()는 반환값 없다!
