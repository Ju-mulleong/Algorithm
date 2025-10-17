import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
자연수 N과 M이 주어졌을 때, 1부터 N까지의 자연수들로 M개의 숫자로 이루어진 중복없는 수열을 구하기

비트마스킹
백트래킹
'''

ans = []

N, M = map(int, input().split())
n_l = list(range(1, N+1))
visited = [0]*(N+1)     # 방문 표시할 N개의 원소를 가진 리스트 (0, 1, 2, ... N) 인데스 쉽게 맞추기 위해서 N+1 길이로 생성


def dfs(sequence, depth):
    # 가지치기

    # 종료조건
    if depth == M:
        ans.extend(sequence)
        return

    # 실행
    for i in range(1, N+1):
        if visited[i] != 1:
            visited[i] = 1

            # 재귀
            dfs(sequence+[i], depth+1,)

            visited[i] = 0
        

dfs([], 0)

l_ans = len(ans)

for a in range(0, l_ans, M):
    print(*ans[a:a+M])

