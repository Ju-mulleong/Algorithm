import sys
sys.stdin = open('input.txt', 'r')


def get_subject_sum(n, k, current_sum, banned_index):
    global min_sum
    # 가지치기
    # 이미 current_sum이 min_sum 이상이면 어차피 최솟값 업데이트 못하므로 return
    if current_sum >= min_sum:
        return

    # print(f'k: {k}, current_sum: {current_sum}, banned_index: {banned_index}')

    # 기본 파트
    if n == k:  # 다 고르면, 합을 지금까지의 최솟값과 비교해서 업데이트
        # print(current_sum)
        if current_sum < min_sum:
            min_sum = current_sum
        return

    # 유도 파트
    else:
        for i in range(N):  # 행에서 한 인덱스 고르기
            if i not in banned_index:
                banned_index.append(i)  # banned_index가 아닌 인덱스일때만 더 깊게 들어가고, 그 인덱스 밴하기
                get_subject_sum(N, k+1, current_sum + arr[k][i], banned_index)
                banned_index.pop()  # 밴 원상복구


'''
한 행에서 하나씩 숫자를 골라서 총 N개 숫자 합의 최솟값 구하기
단, 세로로 같은 줄에서 두 개 이상의 숫자 고를 수 없음.
결국 이것도 나름의 부분집합?인듯

고른 인덱스 ban하고 남은것들 for로?
'''


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    min_sum = 11*N    # 첫 시행에 업데이트 되도록, 10이하의 숫자들만 주어진다
    get_subject_sum(N, 0, 0, [])
    print(f'#{test_case} {min_sum}')