import sys, pprint
sys.stdin = open('input.txt', 'r')
from collections import deque

'''
빨간공과 파란공이 동시에 움직인다.
끝행/열은 막혀있다.
같은 칸에 두 구슬은 들어갈 수 없다.
빨간 구슬을 빼내는 최소 시도수 출력 
10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼수 없으면 -1 출력
최단거리니까 BFS?
'''


def bfs(red_i, red_j, blue_i, blue_j):
    # 초기 deque 만들기
    dq = [(red_i, red_j), (blue_i, blue_j)]

    while dq:
        dq.pop()








    pass


N, M = map(int, input().split())
# N*M 보드

arr = [list(input()) for _ in range(N)]
pprint.pprint(arr)

