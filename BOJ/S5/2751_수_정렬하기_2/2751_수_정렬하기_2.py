import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N개의 수가 주어졌을때, 이를 오름차순으로 정렬하는 프로그램 작성
# 1 <= N <= 1,000,000 이다.
# 시간제한이 2초이므로, 2000ms 안에 끝내야하고, 최대 N = 1000000이므로 시간복잡도가 O(logN)인 방법 사용?
'''
python에서 list의 기본 정렬방법(timsort)의 시간복잡도는 O(nlogn)이다.
'''

N = int(input())
ans = []

for i in range(N):
    ans.append(int(input()))

ans.sort()

print(*ans, sep='\n')

