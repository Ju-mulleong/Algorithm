'''
이진 검색은 항상 정렬된 데이터에 적용.
'''


# 반복을 활용한 이진 검색
def binary_search_while(target):
    # 마찬가지로 left와 right을 좌/우 경계로 설정
    left = 0
    right = len(arr)-1
    cnt = 0     # 문제에서 target 찾기까지의 검색횟수 요구할 경우

    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt     # mid index에서 target 찾음

        # 왼쪽에 정답 있음
        if target < arr[mid]:
            right = mid - 1

        # 오른쪽에 정답 있음
        else:
            left = mid + 1
    # target이 lst내에 없음
    return -1, cnt


# 재귀를 활용한 이진 검색
def binary_search_recur(left, right, target):
    # quick solt와 유사하게, left/right를 작업 영역의 경계로 정한다.
    # left <= right 만족하면 반복
    # left > right 되버리면 return -1

    if left > right:
        return -1

    mid = (left + right) // 2
    # mid에서 target 찾으면 종료
    if target == arr[mid]:
        return mid

    # 한 번 할 때마다 left와 right를 mid 기준으로 이동시켜 주면서 진행
    # 다시 말하자면, left와 right는 좌측 경계, 우측 경계다.

    # mid가 target보다 작으면, left를 mid+1로 옮기기
    if arr[mid] < target:
        # left = mid + 1
        return binary_search_recur(mid+1, right, target)
    # mid가 target보다 크면, right를 mid-1로 옮기기
    else:
        # right = mid - 1
        return binary_search_recur(left, mid-1, target)


arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용해야 한다!!!
arr.sort()  # [2, 4, 7, 9, 11, 19, 23]

print(f'9 - {binary_search_recur(0, len(arr) - 1, 9)}')
print(f'2 - {binary_search_recur(0, len(arr) - 1, 2)}')
print(f'20 - {binary_search_recur(0, len(arr) - 1, 20)}')