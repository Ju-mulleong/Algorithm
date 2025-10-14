import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

'''
병합정렬(nlogn) 직접 구현해보기.
전부 정수 1개 단위로 나누고, 다시 2의 배수로 합친다. 합칠때 정렬
'''

temp = []

for i in range(N):
    temp.append(int(input()))

# while n == 