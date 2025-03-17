import sys
sys.stdin = open('input.txt', 'r')


'''
병합정렬 그냥 하면 된다.
단, 병합과정에서 cnt만 조건에 맞게 세면 됨.
'''


def merge(left_lst, right_lst):
    global cnt
    len_L = len(left_lst)
    len_R = len(right_lst)

    temp_lst = [0]*(len_L + len_R)
    l = r = 0

    # 문제 조건: 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 세기
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    # 어느 한 쪽 비워질 때 까지 반복
    while l < len_L and r < len_R:
        if left_lst[l] < right_lst[r]:      # 왼쪽 인덱스의 값이 더 작으면
            temp_lst[l+r] = left_lst[l]
            l += 1
        else:                               # 오른쪽 인덱스의 값이 더 작거나 같으면
            temp_lst[l+r] = right_lst[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result에 추가
    while l < len_L:
        # 비교하던게 남은거니까.. left[l]
        temp_lst[l + r] = left_lst[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 temp_lst에 추가
    while r < len_R:
        temp_lst[l + r] = right_lst[r]
        r += 1

    # 정렬된 리스트 반환
    # print(temp_lst)
    return temp_lst


def merge_sort(lst):
    # !!!!! 최소단위가 되면, return
    if len(lst) == 1:
        return lst

    # mid 정하고, mid기준으로 left_lst, right_lst 나누기
    mid = len(lst)//2
    left_lst = lst[:mid]
    right_lst = lst[mid:]

    # 최소단위까지 나누기
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    # 다 나눴으면, 정렬해서 병합하기
    merged_lst = merge(left_lst, right_lst)
    return merged_lst   # 다음 병합에 쓰도록 return

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    ans_lst = merge_sort(lst)

    # print(ans_lst)
    print(f'#{test_case} {ans_lst[N//2]} {cnt}')
