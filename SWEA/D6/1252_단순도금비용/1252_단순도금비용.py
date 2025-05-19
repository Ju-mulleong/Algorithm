import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


'''
최소의 비용으로 손상된 모든 부분 도금
금박 필름의 크기는 정해져 있음.

범위 비용
1*1    2
2*2    4
3*3    7     

그리디?
3*3을 가장 많이 쓰는경우가 최소비용?
'''

for test_case in range(1, 1+T):
    # 전체 판의 넓이 S*S
    S = int(input())

    # 손상된 부분의 수 N
    N = int(input())

    # 손상된 부분이 존재하는 구역의 위치(행과 열)
    # 짝수 인덱스가 행, 홀수 인덱스가 열,
    # 0행과 0열은 존재하지 않는다.

    temp_lst = list(map(int, input().split()))
    # print(temp_lst)
    idx_lst = []

    for i in range(0, len(temp_lst), 2):
        idx_lst.append((temp_lst[i], temp_lst[i+1]))
    # print(idx_lst)

