import sys
sys.stdin = open('input.txt', 'r')

# N * M 크기의 행렬이 주어진다.
N, M = map(int, input().split())    # 행렬의 크기 N, M

array_A = [list(map(int, input().split())) for _ in range(N)]      
array_B = [list(map(int, input().split())) for _ in range(N)]
array_C = [[0]* M for _ in range(N)]

# print(array_N)
# print(array_M)

for i in range(N):
    for j in range(M):
        array_C[i][j] = array_A[i][j] + array_B[i][j]

# 출력 형식 똑바로 보자..

for i in array_C:
    print(" ".join(list(map(str, i))))
