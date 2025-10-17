import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
N개의 '정수'가 주어져 있을때, 이 안에 X라는 정수가 존재하는지 알아내기
1 <= N <= 100000
정렬 한 후 찾는게 더 빠른가?
일단 정렬 한 후, target의 최댓값이 original의 최댓값보다 클 경우 --> 컷

아니다 유무만 확인하면되니까 중복 상관없이 set으로 변환 후, in연산(O(1)로 찾기?)
'''

N = int(input())
original = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

ans = []

# print(original, target)

for i in range(M):
    if target[i] in original:
        ans.append(1)
    else:
        ans.append(0)

print(*ans, sep='\n')

