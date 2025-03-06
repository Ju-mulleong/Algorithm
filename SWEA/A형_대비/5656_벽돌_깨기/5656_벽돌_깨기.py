import sys
sys.stdin = open('input.txt', 'r')


'''
벽돌에 숫자 적혀있다.
1은 그냥 돌, 다른 벽돌들은 구슬에 맞거나, 폭발에 맞으면
적힌 숫자 -1 만큼 상하좌우+본인 만큼 폭발한다.

폭발 처리
    맞은 지점 숫자 확인, 1이면 제거
    1제외 다른 숫자(n)이면 
        for i in range(1,n)
            ni = i + di[d]*k
            nj = j + dj[d]*k
    dfs로 일단 다 돌리면서 1번 끝날때 arr 업데이트?
    visited?
    남은 돌 개수 최댓값 업데이트
'''

def dfs(i, j):
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]



def select_shoot_idx(n):
    for j in range(W):
        for i in range(H):
            if arr[i][j] != 0:
                dfs(i, j)








T = int(input())

for test_case in range(1, 1+T):
    N, W, H = map(int, input().split())
    # N은 구슬 발사 횟수, W가 폭, H가 높이인 벽돌들

    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(arr)

    # 구슬 쏘기
    # 선택한 열에서 아래로 쭉 내려서 가장 먼저 찾는 벽돌부터 시작 (!=0)
    for _ in range(N):


