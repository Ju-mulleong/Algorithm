import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 행우선
for i in range(N):
    for j in range(N):
        print(arr[i][j])

# 열우선
for i in range(N):
    for j in range(N):
        print(arr[j][i])    # 정방행렬일때는 i, j만 뒤집으면 된다.

# 지그재그 순회
# 이 버전이 온라인보다 좀 더 직관적이고 이해하기 쉽다.
for i in range(N):
    if i % 2 == 0:      # 짝수행일 때
        for j in range(N):
            print(arr[i][j], end = ' ')

    else:
        for j in range(N-1, -1, -1):
            print(arr[i][j], end = ' ')
    print()
print()