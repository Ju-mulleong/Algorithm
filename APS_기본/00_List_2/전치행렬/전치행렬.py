import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 행우선
for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)

# zip
print(list(zip(*arr)))
# 세로 방향으로 진행, 전치행렬로 바꾼 다음 다음진행.
