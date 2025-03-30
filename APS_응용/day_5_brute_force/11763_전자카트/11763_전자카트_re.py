import sys
sys.stdin = open('input.txt', 'r')


'''
결국 2~N까지의 자연수로 순열 만들기
순열 만드는 방법:
    다중 for문, 재귀, ?
재귀 사용 
'''

# 2~N으로 만들수 있는 순열중 한 가지 주어짐
def cal(fac):
    # 일단 양 끝값 먼저 더하기
    sum_v = arr[1][fac[0]] + arr[fac[-1]][1]

    # 중간에 값들 더하기
    # 주어진 순열 2개씩
    for i in range(len(fac)-1):
        sum_v += arr[fac[i]][fac[i+1]]

    return sum_v


# N이 주어지면, 2~N으로 순열 만들기
def make_factorial(N, fac):
    global min_v, visited
    # print(fac)

    if len(fac) == N-1:
        # 배터리 소비량 계산 함수
        sum_v = cal(fac)
        min_v = min(min_v, sum_v)
        return

    for i in range(2, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        make_factorial(N, fac + [i])
        visited[i] = 0


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N 크기의 배열로 주지만, 더미인덱스 쓰는게 편할듯

    arr = [[0] for _ in range(N+1)]

    for i in range(1, N+1):
        arr[i].extend(list(map(int, input().split())))

    visited = [0] * (1 + N)
    min_v = float('inf')
    make_factorial(N, [])

    print(f'#{test_case} {min_v}')