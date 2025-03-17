'''
1. 분할: 리스트의 길이가 1(최소단위)일때 까지 분할
2. 정복: 리스트의 길이가 1(최소단위)가 되면 자동으로 정렬됨
3. 병합
    - 왼쪽, 오른쪽 리스트 중
        작은 원소부터 정답리스트에 추가하면서 진행(앞에서부터?)
'''

def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    # 둘 중 한 쪽의 리스트라도 먼저 비워지면 종료.
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result에 추가
    while l < len(left):
        # 비교하던게 남은거니까.. left[l]
        result[l+r] = left[l]
        l += 1


    # 오른쪽 리스트에 남은 데이터들을 모두 result에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(li):
    if len(li) == 1:    # 최소단위가 되면, return
        return li

    # 1. 절반 씩 분할
    mid = len(li)//2
    left = li[:mid]     # mid 기준 리스트의 앞쪽
    right = li[mid:]    # mid 기준 리스트의 뒤쪽

    left_lst = merge_sort(left)     # 왼쪽도 분할
    right_lst = merge_sort(right)   # 오른쪽도 분할
    # 결국 최소단위될때까지 계ㅖㅖㅖ속 분할. 좌/우로 나누는 형식

    # 전부 분할됬다면, 병합
    merged_lst = merge(left_lst, right_lst)
    return merged_lst

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)