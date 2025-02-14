import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    '''
    스택으로?
    for i in range(N)
    하나씩 push하고
    if 이번 arr[i]가 top 보다 작다:
        거슬러 올라가서 하나씩 peek해본다.
        peek 값이 arr[i]보다 작아지면 봉우리임.
        
        
        
    
    '''