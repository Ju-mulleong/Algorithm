import sys
sys.stdin = open('input.txt', 'r')

'''
격자판 크기는 4*4로 고정, 격자판에는 0~9 숫자가 적혀있다.
갔었던 칸 다시 가는것도 가능
총 6번 이동, 시작 칸 포함 7자리 숫자 만들기 (0으로 시작도 가능)
BFS? DFS?
'''


def dfs(i, j, temp_str):
    global s
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # 중복방지하기 위해 set 사용
    if len(temp_str) == 7:
        s.add(temp_str)
        return

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        # 정상인덱스라면
        if 0 <= ni <= 3 and 0 <= nj <= 3:
            # 이동하고 이어붙이기
            dfs(ni, nj, temp_str+ f'{arr[ni][nj]}')



T = int(input())

for test_case in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    s = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, f'{arr[i][j]}')

    print(f'#{test_case} {len(s)}')

'''
set의 메서드 기억,
.add() .update()
'''