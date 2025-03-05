'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

import sys
sys.stdin = open('input.txt', 'r')

# 전위순회
def pre_order(T):
    if T:                   # T가 존재한다면!(0이 아니라면)
        print(T, end = ' ')     # 노드 방문시 할 일
        pre_order(left[T])      # 왼쪽 자식 방문
        pre_order(right[T])     # 오른쪽 자식 방문

# 중위순회
def in_order(T):
    if T:                   # T가 존재한다면!(0이 아니라면)
        in_order(left[T])      # 왼쪽 자식 방문
        print(T, end=' ')  # 노드 방문시 할 일
        in_order(right[T])     # 오른쪽 자식 방문

# 후위순회
def post_order(T):
    if T:                   # T가 존재한다면!(0이 아니라면)
        post_order(left[T])      # 왼쪽 자식 방문
        post_order(right[T])     # 오른쪽 자식 방문
        print(T, end=' ')  # 노드 방문시 할 일


# 부모를 인덱스로 자식 노드를 저장
N = int(input())    # 1번부터 N번까지인 정점
lst = list(map(int, input().split()))

E = N-1     # 간선수는 노드 수 -1
left = [0]*(N+1)    # 더미 인덱스 포함
right = [0]*(N+1)   # 더미 인덱스 포함
par = [0]*(N+1)


for i in range(E):
    p, c = lst[i*2], lst[i*2+1]
    # p는 부모, c는 자식
    par[c] = p          # 자식을 인덱스로 부모 저장
    if left[p] == 0:    # 아직 왼쪽 자식 안채웠으면
        left[p] = c
    else:
        right[p] = c


root = 1
for i in range(1, N+1):
    if par[i] == 0:     # 부모 정점이 없으면 루트
        root = i
        break

print(left)
print(right)
pre_order(1)    # 1번부터 전위순회
print()
pre_order(3)    # 3번부터 전위순회
print()
print(f'root: {root}')