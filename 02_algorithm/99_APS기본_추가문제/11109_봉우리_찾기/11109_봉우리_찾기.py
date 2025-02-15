import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    if N == 1:
        print(f'#{test_case} {1}')
        continue
    lst = [arr[0]]  # arr의 첫 원소 추가
    # print(arr)

    '''
    스택으로?
    for i in range(N)
    하나씩 push하고
    if 이번 arr[i]가 top 보다 작다:
        거슬러 올라가서 하나씩 peek해본다.
        peek 값이 arr[i]보다 작아지면 봉우리임.
        
    현재 높이와 다음 높이가 같을 경우, pass
        다른 경우 append한다.
        그래서 리스트 다 만들고 비교하면 된다.
        첫항과 끝항만 따로 보자. 중복제거했으니까
    '''

    if len(arr) != 1 :
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                pass
            else:
                lst.append(arr[i])

    # print(lst)
    cnt = 0
    # len(lst) = 10
    for i in range(len(lst)): # 0 ~ 9
        if i == 0 :
            if lst[i] > lst[i+1]:
                cnt += 1
        elif i == (len(lst)-1):
            if lst[i] > lst[i-1]:
                cnt += 1
        else:
            if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
                cnt += 1


    # print(lst)`
    print(f'#{test_case} {cnt}')
