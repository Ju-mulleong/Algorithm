'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

'''
1과 2가 인접해있으면, 당연히 2와 1도 인접해있다. 같은말
이걸 이차원배열안에 표현 가능

비어있는 인접리스트 생성 (adj_list)

i행에 저장
    i번 정점에 인접한 정점 번호

저 1 2 1 3... 읽는법
    영상 보자. 인덱스에 곱하거나 더하거나 하기

'''

def dfs(v, N):
    visited = [0] * (N+1)       # 입력조건 잘 보고 하기
    stack = []

    while True:
        if visited[v] == 0:     # 첫 방문이면
            visited[v] = 1
            print(v)

        for w in adj_list[v]:   # v에 인접하고 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)     # 현재 정점 push
                v = w           # w로 이동
                break           # for w

        else:                   # 남은 인접한테 방문 안한 곳이 없을 경우
            if stack:
                v = stack.pop()
            else:
                break           # while True


V, E = map(int, input().split())
graph = list(map(int, input().split()))
