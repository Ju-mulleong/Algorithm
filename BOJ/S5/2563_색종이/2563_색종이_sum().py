import sys
sys.stdin = open('input.txt', 'r')

'''
    이건 도화지 전체를 0을 원소로 가진 100 * 100의 배열로 만들고,
    색종이 부분을 1로 바꾸는 방법

    어차피 내장함수 안 쓰는건 SSAFY가서 많이 하니까 집에서는 쓰는 연습을 하자
'''

T = int(input())  # 테스트 케이스의 개수 T

N = 10
# 색종이의 크기는 10 * 10

M = 100
# 도화지의 크기는 100 * 100

arr = [[0] * M for _ in range(M)]

for test_case in range(1, 1 + T):
    dj, di = map(int, input().split())  # dj는 도화지의 왼쪽 변과의 거리, di는 아래쪽 변과의 거리

    for j in range(dj, dj + 10):
        for i in range(di, di + 10):
            arr[j][i] = 1

ans = 0
for i in arr:
    ans += sum(i)   # 이차원 배열 arr을 행마다 ans에 합산
print(ans)









