import sys
import pprint
sys.stdin = open('input1.txt', 'r')


'''
출력값: 만들 수 있는 가장 긴 등산로의 길이
가장 높은 봉우리 찾기. 거기서 DFS 시작
    조건: 현재높이보다 낮아야 함
        경로 길이를 기억해야한다.
        visited를 +=1씩 해서 할당한다.
        더 이상 나보다 낮은곳이 없어서 return해야하면 그 자리에 현재까지의 길이 할당
        만약 같은 자리에 도착한 경우 그 중 최댓값 할당
        
    여기서 높이를 깎는걸 어떻게 할 것인가?
    
    DFS에 높이 깎는과정 끼워넣기?
    깎았을때, 안 깎았을 때 비교해서 
        
    ! 막히는 칸 만났을 때, 
        아직 안 깎았는가?(flag == 1)
            깎아서 갈 수 있는가?
                모두 통과하면 플래그 내리고 깎아서 visited 하기.
                그러면 다시 막히는 칸 만날텐데. 거기서 return
    
    더 이상 갈 수 없을 때의 값만 계속 최댓값과 비교해서 업데이트
    visited에 마지막 도착 했을때 할당 안해도 됨
'''


def find_highest_idx(arr):
    # 이차원 배열에서 최댓값 구하기
    high = max(map(max, arr))
    # print(high)
    high_lst =[]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == high:
                high_lst.append([i, j])
    return high_lst


def dfs(i, j):
    global flag, max_v, visited, K
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    # print(i, j)
    # 현재 위치에서 상하좌우 중, 정상인덱스이면서 현재값보다 낮은 위치 확인
    # 정상인덱스면서 나보다 큰 값이라면, 깎아서 갈 수 있는지 확인
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni <= N-1 and 0 <= nj <= N-1 and (visited[ni][nj] == 0):   # 정상인덱스이고, 방문하지 않았다면
            if arr[i][j] > arr[ni][nj]:     # 현재위치가 목표위치보다 높고, 방문하지 않았다면 이동
                visited[ni][nj] = visited[i][j] +1      # visited에 지나온 경로만큼의 길이값 표시
                # pprint.pprint(visited)
                dfs(ni, nj)                             # 재귀(이동)
                visited[ni][nj] = 0                     # visited 원복

            else:       # 목표위치가 현재 높이보다 높거나 같을 때
                if arr[ni][nj]-K < arr[ni][nj]:     # 목표위치의 높이를 K만큼 깎았을때 현재위치 높이보다 낮다면
                    if flag == 1:               # 만약 아직 안 깎았다면

                        for dig in range(1, K+1):   # 깎을 수 있는 경우의 수     # 1,2,3...K
                            arr[ni][nj] -= dig

                            if arr[ni][nj] < arr[i][j]:     # 깎은 높이가 현재 높이보다 낮다면
                                flag = 0
#                                 print(f'dig={dig}')

                                visited[ni][nj] = visited[i][j] + 1     # visited에 지나온 경로만큼의 길이값 표시
#                                 pprint.pprint(visited)
                                dfs(ni, nj)                             # 재귀(이동)
                                visited[ni][nj] = 0                     # visited 원복
                                flag = 1                                # flag 원복
#                                 print(i, j)

                            arr[ni][nj] += dig                          # arr[ni][nj] 높이 원복

                    else:   # 이미 깎았다면, 목표위치로 이동 못하므로 다른 방향 탐색
                        continue

                elif arr[ni][nj]-K > arr[ni][nj]:       # 목표위치를 K만큼 깎아도 현재위치 높이보다 높다면 다른 방향 탐색
                    continue

        else:   # 정상인덱스가 아니라면
            continue

    # 4방향 다 탐색했는데 이동 못했다면, 그 좌표가 그 등산로의 도착지점
    # 최댓값 업데이트
    max_v = max(max_v, visited[i][j])
#     print(f'max_v ={max_v}')
    return


T = int(input())

for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    # 지도는 N*N 크기,
    # K는 최대 공사 가능 깊이

    # 산 2차원 배열 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 등산로 길이 기억할 visited
    visited = [list([0]*N) for _ in range(N)]
    # pprint.pprint(visited)

    # 가장 높은 봉우리의 인덱스로 이루어진 이차원 리스트
    high_lst = find_highest_idx(arr)
    # print(high_lst)

    flag = 1
    max_v = 0

    for i, j in high_lst:
        # print(i, j)
        visited[i][j] = 1
        dfs(i, j)
        visited[i][j] = 0

    # pprint.pprint(visited)
    print(f'#{test_case} {max_v}')