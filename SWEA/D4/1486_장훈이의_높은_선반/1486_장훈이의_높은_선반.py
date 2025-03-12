import sys
sys.stdin = open('input.txt', 'r')

'''
높이가 B이상인 탑 중에서 가장 낮은 탑 구하기
비트마스킹?
1 <= Hi <= 10,000
비트마스킹으로 키의 합 조합 만들고, 
    선반과 비교, 선반보다 높으면
        최솟값과 비교해서 업데이트
'''

T = int(input())

for test_case in range(1, 1+T):
    N, B = map(int, input().split())

    lst = list(map(int, input().split()))

    min_v = 200000  # 점원의 수 최댓값 20, 점원의 키 최댓값 10000
    for i in range(1 << len(lst)):      # lst의 모든 부분집합 생성
        sum_v = 0
        for j in range(len(lst)):       # lst의 모든 원소에 대해 확인
            if i & (1 << j):
                sum_v += lst[j]         # 해당비트가 1이면, 탑에 합산

        # 탑을 다 쌓은 뒤
        if sum_v >= B:   # 만약 탑의 높이가 선반보다 높거나 같으면
            # 최솟값과 비교해서 업데이트
            if min_v > sum_v:
                min_v = sum_v

    # print(min_v, B)
    print(f'#{test_case} {min_v - B}')
