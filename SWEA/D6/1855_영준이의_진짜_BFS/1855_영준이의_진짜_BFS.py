import sys
sys.stdin = open('input.txt', 'r')


'''
모든 가중치가 1인 간선들?
최단거리로 이동했을 때, 가중치의 총 합
입력 헷갈리는데, 
    그냥 2부터 시작해서 N번노드까지 (=i)
    각 노드들의 부모노드를 입력받는 것
    첫번째 tc를 보면 2, 3번 노드의 부모는 1번, 4번 노드의 부모는 2니까 '1 1 2'로 받는다.
'''


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 노드의 개수 N

