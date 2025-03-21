import sys
sys.stdin = open('input.txt', 'r')

'''
모든 열이 연속된글자가 3개 이상 존재하는 경우가 최소 한번 있어야함.
DFS? 13팩토리얼
가지치기 조건
그냥 매번 시행해서
'''


# 성능검사
def check(arr):
    global K
    for j in range(width):
        cnt_same = 1
        flag_k = 0
        for i in range(height - 1):
            target = arr[i][j]
            if arr[i+1][j] == target:
                cnt_same += 1

            else:
                cnt_same = 1

            if cnt_same == K:
                flag_k = 1
                break

        if flag_k == 0:
            return False

    return True


def dfs(cnt, n, arr):
    # print(cnt)
    global min_v

    # 성능검사 실행
    # 성능검사 통과했으면, 약품 투입 횟수 최솟값 업데이트
    if check(arr) is True:
        min_v = min(min_v, cnt)
        return

    # 최악의 경우, 모든 행에 약을 칠지 말지 선택했다면, return
    if n == height:
        return

    # 가지치기
    # 이미 약 바른 횟수가 현재 기준 최솟값을 넘어갔거나 같으면, return
    if cnt >= min_v:
        return


    # 원본 행 저장
    original_row = arr[n]
    # print(original_row, cnt)

    # 약 적용 안함(다음 열로 넘어감)
    dfs(cnt, n+1, arr)

    # A약 적용
    arr[n] = [0] * width
    dfs(cnt + 1, n+1, arr)

    # B약 적용
    arr[n] = [1] * width
    dfs(cnt + 1, n+1, arr)

    # 원복
    arr[n] = original_row
    # print(original_row, cnt)


T = int(input())

for test_case in range(1, 1+T):
    height, width, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(height)]
    # print(arr)

    # 몇 행을 이미 약을 쳤는가
    min_v = float('inf')

    dfs(0, 0, arr)

    print(f'#{test_case} {min_v}')


'''
DFS는 무조건 현재 상태가 답이 될 수 있는지를 가장 먼저 검사하자...
'''