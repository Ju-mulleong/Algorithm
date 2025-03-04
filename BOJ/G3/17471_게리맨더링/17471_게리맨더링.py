import sys
sys.stdin = open('input1.txt', 'r')


'''
dfs의 매개변수를 두 선거구로 받기
    공집합 제외
'''

def is_connecting(subset):
    # 부분집합의 노드들이 전부 이어져 있는가?
    # subset = [5, 2, 3, 4], bit = [0, 1, 1, 1, 1, 0, 0], 1번/2번/3번/4번 노드로 이루어진 부분집합
    # adj_lst에서 노드번호들의 행 확인, 그 행들에 부분집합의 노드번호들이 포함되 있는지 확인

    bit_check = [0]*(N+1)
    for i in range(1, N+1):
        if bit[i] == 1:
            for j in adj_lst[i]:
                bit_check[j] = 1


    # 전부 이어졌다면 1 return, 그렇지 않으면 0 return



def gerry(n, k, subset_1, subset_2):
    global min_v, cnt
    # 가지치기
    # 부분집합이 서로 연결 될때만 가능하도록
    pass

    # 기본 파트
    if n == k:
        if subset_1 != [] and subset_2 != []:   # 공집합 아니라면

            # 각 부분집합끼리 서로 연결되어있는지 확인
            if



            cnt += 1
            # 부분집합 완성되면, 인구 사이의 최솟값 구하기
            min_temp = sum(subset_1) - sum(subset_2)
            if min_v > min_temp:   # 최솟값 업데이트
                min_v = min_temp

            return
        return
    # 유도 파트
    bit[k] = 1
    gerry(n, k+1, subset_1 + [nodes[k]], subset_2)

    bit[k] = 0
    gerry(n, k+1, subset_1, subset_2 + [nodes[k]])



N = int(input())    # 구역의 개수(노드 수) N

nodes = [0]
nodes.extend(list(map(int, input().split())))
bit = [0]*(N+1)
# print(nodes)

# 양방향 인접리스트 만들기
adj_lst = [[0] for _ in range(1+N)]     # 더미 0번 행 포함

for i in range(1, 1+N):
    adj_lst[i] = (list(map(int, input().split()))[1::])

print(adj_lst)
min_v = 0
cnt = 0
gerry(N+1, 1, [], [])

if cnt == 0:
    print(-1)
else:
    print(min_v)

'''
처음엔 bit[] 안쓸려고 했는데 부분집합이 서로 이어져 있는지 확인할려면 쓰는게 나을듯
'''