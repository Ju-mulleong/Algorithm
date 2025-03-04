import sys
sys.stdin = open('input1.txt', 'r')




def get_subset():







N = int(input())
# N은 구역의 개수

nodes = [0]
nodes.extend(list(map(int, input().split())))   # 더비 0번노드 포함해서 nodes 만들기, 1번 노드의 인구는 5명..
# print(nodes)

# 인접리스트 생성
adj_lst = [[0] for _ in range(N+1)]
for i in range(1, 1+N):
    adj_lst[i] = list(map(int, input().split()))[1::]
# print(adj_lst)

'''
가능한 부분집합을 전부 만든다.
     원소의 개수: 1 ~ n//2만 하면됨. 남는건 자동으로 다른 부분집합.
     부분집합이 전부 연결되어있는지 확인한다.
     두 부분집합간 인구 차이의 최솟값을 구한다.
'''
