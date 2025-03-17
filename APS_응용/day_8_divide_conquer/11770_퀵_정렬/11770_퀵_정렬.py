import sys
sys.stdin = open('input.txt', 'r')


'''
퀵 정렬
    pivot 정하고, 좌/우 가르고, 범위에서 i는 left, j는 right에서 시작(양끝)
    i에서 pivot보다 큰 값과 j에서 pivot보다 작은값 swap
    i와 j가 교차될 때 까지 반복
    
    pivot j 위치로 옮기기(pivot = left 기준)
    반복..
'''

# partitioning
def hoare_partitioning(left, right):
    # 가장 왼쪽 값 p 설정
    p = left
    i = left + 1
    j = right

    '''
    왜 i <= j 일때도 있고, i < j 도 있나?
    그려보면 나오는데, 만약 i와 j가 같은 칸에서 만난 경우, 
    i와 j 둘 중하나는 뒤로 가거나 앞으로 간다.
    p와 같은 값은 없으므로..
    만약 같은 칸(= same)에서 값이 p보다 작으면, 
        i는 지금까지 하던것처럼 한 칸 더 간다. 그리고 멈춘다. j가 지나온 길이니까 p보다 큰값이다.
        하지만 j는 same에서 멈춰있다. j는 p보다 작은값을 만날때 멈추므로
        그러면 j와 i가 교차되고, 하던대로 j와 p자리를 바꾸면 정렬된다.
    
    p가 클때도 마찬가지. 이번엔 i가 가만있고 j가 same보다 한 칸 더 가서 교차된다.
    이런걸 어떻게 생각? respect
    '''

    while i <= j:
        while i <= j and lst[i] <= lst[p]:   # 계속 넘어가다가 p보다 크거나 같은 값나오면 멈추도록
            i += 1

        while i <= j and lst[j] >= lst[p]:   # 계속 넘어가다가 p보다 작거나 같은 값 나오면 멈추도록
            j -= 1

        '''
        lst[i] <= lst[p]
        같은 값일때도 SWAP해서, p를 같은 값들 중 가장 앞으로 오도록(같은값도 정렬되게)
        '''
        # SWAP
        if i < j:   # i와 j가 다른 인덱스일때만 SWAP? 의미있나?
            lst[i], lst[j] = lst[j], lst[i]

    # 교차되면, pivot 옮기기
    lst[j], lst[p] = lst[p], lst[j]
    return j


# 퀵 정렬
def quick_sort(left, right):
    # right가 left보다 클때만 실행(1칸일때는 그냥 return되도록)
    if left < right:

        # pivot 위치 정하기 (주어진 구역의 정렬도 같이)
        pivot = hoare_partitioning(left, right)
        # pivot 기준으로 왼쪽을 탐색 구역으로
        quick_sort(left, pivot-1)
        # pivot 기준으로 오른쪽을 탐색 구역으로
        quick_sort(pivot+1, right)


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 주어진 정수의 개수 N

    lst = list(map(int, input().split()))

    quick_sort(0, len(lst)-1)
    # print(lst)
    print(f'#{test_case} {lst[N//2]}')