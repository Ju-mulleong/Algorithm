import sys
sys.stdin = open('input.txt', 'r')

# 9 * 9 격자판에 81개의 자연수 또는 0 주어짐
# 그 중 최댓값을 찾고, 그 최댓값이 몇 행 몇 열에 위치하는지 구하기


# input값으로 2차원 배열 만들기
arr = [list(map(int, input().split())) for _ in range(9)]
# print(arr)

# 최댓값의 위치 찾기
max_value = 0     # input으로 주어지는 수는 0이상의 정수
max_value_i = 0
max_value_j = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_value:
            max_value = arr[i][j]
            max_value_i = i + 1     # 1행 ~ 9행   행은 인덱스에서 + 1
            max_value_j = j + 1     # 1열 ~ 9열   열은 인덱스에서 + 1

print(max_value)
print(max_value_i, max_value_j)

'''
arr[i][j] > max_value 로 하면
격자판의 81칸 전부 0 일때 max_value_i, max_value_j 가 업데이트 안 됨. 

'''
