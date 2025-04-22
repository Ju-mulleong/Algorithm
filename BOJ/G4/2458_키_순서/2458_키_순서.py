import sys
sys.stdin = open('input2.txt', 'r')     # input1.txt, input2, input3
from collections import deque


'''
자신의 키를 알 수 있다
     모든 노드들과 닿을 수 있다? 아닌듯
     1번은 3번과의 키 비교 불가
     
     자신을 통과해서 모든 노드를 단방향으로 탐색 가능할 때?
     4번 기준으로 1,3,5가 자신을 통해서 들어오고 / 2,6번으로 나갈 수 있다.
     
     5번은 1번보다 크고 2,4,6이 자기보다 크지만 3번 파악 불가
     
    자신 기준 조상 노드의 수 + 자식 노드의 수 + 1 = 전체 노드의 수
    이면 자신의 키 순서 파악 가능. 
'''


def solve(i):
    # 나의 모든 자손노드의 수 + 나의 모든 조상노드의 수 + 1 == N이면 키 순서 아는 것
    # print('-----------------------')
    # 1(자신)
    cnt = 1
    # print(cnt)
    # 상관없을거같긴한데 안전하게 리스트 컴프리헨션으로 부모 노드 번호들 복사
    dq = deque(x for x in p_lst[i])

    # visited
    visited = [0]*(1+N)

    while dq:
        # print(dq)
        # dequeue
        cur_node = dq.popleft()
        # print(cur_node)
        # 이미 체크했던 노드면, 넘기기
        if visited[cur_node]:
            continue

        cnt += 1
        visited[cur_node] = 1
        # print(f'cnt={cnt}')

        # print(cur_node)
        # 부모 노드 개수 카운트
        if len(p_lst[cur_node]):    # 부모가 존재한다면
            for pp in p_lst[cur_node]:
                if visited[pp]:
                    continue
                dq.append(pp)

    dq = deque(x for x in s_lst[i])

    visited = [0] * (1 + N)

    while dq:
        # print(dq)
        # dequeue
        cur_node = dq.popleft()
        # print(cur_node)
        # 이미 체크했던 노드면, 넘기기
        if visited[cur_node]:
            continue

        cnt += 1
        visited[cur_node] = 1
        # print(f'cnt={cnt}')

        # print(cur_node)
        # 부모 노드 개수 카운트
        if len(s_lst[cur_node]):  # 부모가 존재한다면
            for ss in s_lst[cur_node]:
                if visited[ss]:
                    continue
                dq.append(ss)

    # print(f'최종 cnt = {cnt}')
    if cnt == N:
        # print(f'i = {i}')
        return True


# N은 학생들의 수, M은 키를 비교한 횟수
N, M = map(int, input().split())

# 자식을 저장할 리스트, 부모를 저장할 리스트 만든다.
# 나보다 키가 더 큰 노드는 자식노드
p_lst = [[] for _ in range(N+1)]
s_lst = [[] for _ in range(N+1)]

for _ in range(M):
    p, s = map(int, input().split())
    s_lst[p].append(s)  # p인덱스 리스트의 자식 저장
    p_lst[s].append(p)  # s인덱스 리스트의 부모 저장

# print(s_lst)
# print(p_lst)
ans = 0

for i in range(1, N+1): # N명이면, 1번부터 N번까지의 학생
    if solve(i) is True:
        ans += 1

print(ans)
