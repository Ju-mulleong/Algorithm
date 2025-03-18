import sys
sys.stdin = open('input.txt', 'r')


'''
list_b에 속한 어떤 수가 list_a에 들어있으면서 ,
그 수가 동시에 탐색 과정에서 양쪽 구간을 번갈아 선택하게 된다면, cnt += 1
cnt 출력
'''


def binary_search(left, right, target, flag):
    global cnt
    # left > right 되버리면 return -1

    if left > right:
        return -1

    # mid 정하기
    mid = (left+right)//2

    # mid가 target인지 확인
    if target == list_a[mid]:
        cnt += 1
        return

    # 이진탐색 하되, 구역을 번갈아서 탐색 했을 경우에만 실행

    # target이 mid보다 크다면, mid의 오른쪽을 탐색구간으로
    if target > list_a[mid]:
        # 만약 전 시행에서도 mid의 오른쪽을 골랐다면, 문제 조건에 안맞음. return
        if flag == 'L':
            return
        binary_search(mid+1, right, target, 'L')
    # target이 mid보다 작다면, mid의 왼쪽을 탐색구간으로
    else:
        # 만약 전 시행에서도 mid의 왼쪽을 골랐다면, 문제 조건에 안맞음. return
        if flag == 'R':
            return
        binary_search(left, mid-1, target, 'R')


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 list_a의 길이, M은 list_b의 길이

    list_a = sorted(list(map(int, input().split())))
    list_b = list(map(int, input().split()))
    cnt = 0

    for target in list_b:
        binary_search(0, len(list_a) - 1, target, 0)

    print(f'#{test_case} {cnt}')


'''
문제 똑바로 보기, 보이는 testcase에서는 정렬해서 주지만, 
자세히보면 주어진 N을 정렬해서 쓰라고 되있다.

그리고 "m에 찾는 원소가 있는 경우 방향을 따지지 않는다" 이건 왜들어간거야?
'''