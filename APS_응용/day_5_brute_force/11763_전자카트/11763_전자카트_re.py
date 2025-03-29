import sys
sys.stdin = open('input.txt', 'r')


'''
결국 2~N까지의 자연수로 순열 만들기
순열 만드는 방법:
    다중 for문, 재귀, ?
재귀 사용 
'''


def make_pactorial():

    pass

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N 크기의 배열로 주지만, 더미인덱스 쓰는게 편할듯

    arr = [[0] for _ in range(N+1)]

    for i in range(1, N+1):
        arr[i].extend(list(map(int, input().split())))



