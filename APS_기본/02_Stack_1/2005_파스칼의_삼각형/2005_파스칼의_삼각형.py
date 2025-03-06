import sys
import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())

def f(N):
    if N == 1:       # 종결조건
        return [1]

    if N == 2:
        return [1, 1]

    if N > 1:
        lst = [0]*N
        for i in range(N):
            if i == 0 or i == N-1:
                lst[i] = 1
            else:
                lst[i] = f(N-1)[i-1] + f(N-1)[i]
        if lst not in arr:
            arr.append(lst)
        return lst


for test_case in range(1, 1+T):
    N = int(input())    # 크기가 N인 파스칼의 삼각형

    # 출력할 때 모양 신경 안 쓰고 왼쪽정렬해서 출력해도 됨.

    # 파스칼의 삼각형은 이차원 배열
    arr = [[1], [1, 1]]
    # pprint.pprint(arr)

    '''
    재귀인듯?
    
    재귀반복해서 차례대로 출력하도록?
    return을 한 줄마다 하도록하면 함수 한번 호출하면 크기만큼 출력한다.
    N = 4이면 4번 출력하도록
    
    '''


    '''
    def f(N, row, column):   # N = 3   크기가 N인 파스칼의 삼각형 arr의 row행 column열 숫자 만들기
        if column == 0 or column  == N-1:
            return 1
        
        for i in range(N):  # i = 0,1,2
            if i == 0 or i == N-1:
                return 1
    
            else:
                arr[N-1][i] = f(N-1)
    
    
            arr[N] = [1, arr[N-1][0] + arr[N-1][1], arr[N-1][1] + arr[N-1][2],..... 1]
            arr[N] 의 원소는 N+1개
    
    '''

    print(f'#{test_case}')
    f(N)
    if N == 1:
        print(1)
    else:
        for i in arr:
            for j in i:
                print(j, end=' ')
            print()

    # pprint.pprint(arr)

