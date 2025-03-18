import sys
sys.stdin = open('input.txt', 'r')

'''

'''

def dfs(n, charge, cnt):    # 현재 인덱스(정류장 번호), 충전량, 교환횟수
    # print(n, charge, cnt)
    global min_v
    
    # 종료조건
    # 충전량이 -1인경우, 배터리 방전인데 왔다는 뜻이니까 옳지 않은 경로
    if charge == -1:
        return

    # 만약 현재 충전량 + 현재 인덱스가 목적지 인덱스보다 크거나 같은 경우
    if charge + n >= N:
        # 교체횟수 최솟값과 비교하여 업데이트
        # print(n, cnt)
        min_v = min(min_v, cnt)
        return

    # 가지치기
    # 현재 교환횟수가 이미 최솟값인 교환횟수보다 크거나 같으면 return (같은 경우, 위에서 종료되지 않았으므로 더 가야하니까)
    if cnt >= min_v:
        return

    # 이번 정류장에서 충전 하는 경우 (교체용 충전기이다)
    dfs(n+1, lst[n]-1, cnt + 1)

    # 이번 정류장에서 충전 안 하는 경우
    dfs(n+1, charge-1, cnt)


T = int(input())

for test_case in range(1, 1+T):
    lst = list(map(int, input().split()))   # lst[0]은 정류장 수
    N = lst[0]  # 정류장 수와 목적지의 인덱스가 같다!
    min_v = 0xfffff

    dfs(1, lst[1], 0)     # 첫 정류장에서 충전하고 시작.
    print(f'#{test_case} {min_v}')