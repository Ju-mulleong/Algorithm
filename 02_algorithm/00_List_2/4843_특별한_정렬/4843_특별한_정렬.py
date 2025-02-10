import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1+T):
    N = int(input())    # 정수의 개수 N
    arr = list(map(int, input().split()))   # N개의 정수들

    # 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수.... 이렇게 정렬해야함.
    '''
    1. 가장 큰 수와 가장 작은 수를 번갈아서 pop하면 될꺼같은데
    2. 오름차순으로 정렬한 다음에 for로 index를 번갈아서 하면 될거같다.
        선택정렬을 변형시키면 될 듯.
    
    1번은 매번 리스트를 탐색해야되고, 2번은 한 번만 정렬하면 된다.
    매번 탐색과 한 번 정렬중에 뭐가 더 빠른가?
    '''

    # 10 <= N <= 100, 1 <= arr의 원소 <= 100

    # 2번으로 해보자.
    # 선택정렬

    flag = 'max'   # 최댓값 계산 먼저

    # 아래 for문 step을 2로 할까 생각했는데 len(arr)이 홀수이면 귀찮아질꺼같아서 플래그변수 쓰기로 함
    for target in range(len(arr)):  # target 기준위치

        if flag == 'max':
            idx = target  # 기준위치로 초기화
            # 최댓값 계산
            max_v = 0
            for i in range(target, len(arr)):
                # 기준위치 target ~ 끝위치 최댓값 찾기
                if arr[i] > max_v:
                    max_v = arr[i]  # 최댓값 업데이트
                    idx = i  # 최댓값 위치 업데이트

            arr[target], arr[idx] = arr[idx], arr[target]  # 최댓값 기준 위치로 밀기
            flag = 'min'

        elif flag == 'min':
            idx = target + 1  # 기준위치로 초기화
            # 최솟값 계산
            min_v = 100
            for i in range(target, len(arr)):
                # 기준위치 target ~ 끝위치 최솟값 찾기
                if arr[i] < min_v:
                    min_v = arr[i]
                    idx = i

            arr[target], arr[idx] = arr[idx], arr[target]  # 최솟값 기준 위치로 밀기
            flag = 'max'

    ans = ''
    for i in arr[:10]:
        ans += f'{str(i)} '

    print(f'#{test_case} {ans}')






