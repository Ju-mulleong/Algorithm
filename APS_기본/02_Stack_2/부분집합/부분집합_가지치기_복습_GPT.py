'''
원소들의 총 합이 30 이하인 부분집합의 개수 구하고,
그 부분집합들의 종류와 합 모두 출력
'''

def sum_of_set(n, k, sum_v, subset):
    global cnt

    # 가지치기: 합이 30 초과하면 탐색 중지
    if sum_v > 30:
        return

    # 기본 파트: 모든 요소를 확인했을 때
    if k == n:
        if sum_v > 0:  # 공집합 제외
            cnt += 1
            print(f'부분집합: {subset} 원소들의 합: {sum_v}')
        return

    # 유도 파트: 현재 원소를 포함하는 경우
    sum_of_set(n, k + 1, sum_v + arr[k], subset + [arr[k]])

    # 유도 파트: 현재 원소를 포함하지 않는 경우
    sum_of_set(n, k + 1, sum_v, subset)


cnt = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_set(len(arr), 0, 0, [])
print(f'합이 30이하인 부분집합들의 총 개수: {cnt}')
