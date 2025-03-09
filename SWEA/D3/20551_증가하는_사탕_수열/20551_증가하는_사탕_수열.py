import sys
sys.stdin = open('input.txt', 'r')


'''
A, B, C  세 개 안에 있는 사탕의 개수가 오름차순이도록
공집합 XX
사탕을 최소한으로 먹어서 없애는 것(0개 이상)
조건 만족 불가시 -1, 이미 만족이면 0, 1개 이상 먹어서 조건 만족 가능하면 먹은 숫자
최소한으로 먹어야하니까 C는 건드리지 않아도 된다.
dfs?  1 <= a,b,c <= 3000

그냥 b를 c-1과 같게하고 a를 b-1과 같게 한다?
'''

def solve(a, b, c):
    global cnt

    # 조건 만족하면 끝
    if a < b < c:
        return

    if b != c-1:
        bb = c-1
        cnt += b - bb
        solve(a, bb, c)

    elif a != b-1:
        aa = b-1
        cnt += a - aa
        return


T = int(input())

for test_case in range(1, 1+T):
    A, B, C = map(int, input().split())
    cnt = 0
    # c가 3보다 작은 경우 조건 만족 불가, B가 2보다 작은 경우 조건 만족 불가
    if C < 3 or B < 2:
        print(f'#{test_case} {-1}')
        continue

    else:
        solve(A, B, C)
        print(f'#{test_case} {cnt}')




