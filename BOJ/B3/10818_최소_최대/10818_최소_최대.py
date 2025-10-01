import sys
sys.stdin = open('input.txt', 'r')

'''
첫째 줄에 정수의 개수  1 <= N <= 1,000,000
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 

첫째줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력

1. 입력 한번에 받은 후 최소/최대 찾기

2. 하나씩 받을때마다 최소/최대 구하기

메서드 쓸거? 일단 안쓰고 ㄱㄱ

'''

# T = int(input())

N = int(input())

nums = list(map(int, input().split()))
# print(nums)

min_v = 1000000
max_v = -1000000

for i in range(N):
    if nums[i] < min_v: 
        min_v = nums[i]
    if nums[i] > max_v:
        max_v = nums[i]

print(min_v, max_v)
