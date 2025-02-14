import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def fac(num):
    ans = 1
    for i in range(1, num+1):
        ans = ans * i
    return ans

def solve(N):
    Max_M = N // 10
    cnt = 0
    # M은 10*20 색종이의 개수
    # P는 M을 고정했을때 10*20의 개수

    if Max_M % 2 == 0:  # Max_M이 짝수이면
        for M in range(0, Max_M+1, 2):
            P = (N - (M * 10)) // 20  # P는 무조건 정수여야함

            cnt += (fac(M + P) * 2 ** P) // (fac(M) * fac(P))
            # print(cnt)

    else:           # Max_M이 홀수이면
        for M in range(1, Max_M+1, 2):
            P = (N-(M*10)) // 20    # P는 무조건 정수여야함

            cnt += (fac(M+P) * 2 ** P) // (fac(M) * fac(P))

    return cnt


for test_case in range(1, 1+T):
    N = int(input())

    print(f'#{test_case} {solve(N)}')