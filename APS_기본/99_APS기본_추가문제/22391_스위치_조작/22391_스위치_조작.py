import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1+T):
    N = int(input())    # 전등의 개수 N

    arr_init = list(map(int, input().split()))      # 초기 전등 상태 arr_init
    arr_obj = list(map(int, input().split()))       # 목표 전등 상태 arr_obj

    # 인덱스 기준 0 ~ N-1 번의 전구들
    # i번 스위치 키면 i번 ~ N-1번 전구들 상태가 바뀐다.
    # 최소 몇 번 스위치를 조작해야 하는가?

    # 1과 0이 아니라 스위치 켤때마다 값 +1 해서 홀수, 짝수로 생각하면?
    # 아니다 그냥 하나씩 1을 남길수 있다고 생각하자.
    '''
    예를 들어 arr_init = 00000, arr_obj = 00101 이라고 한다면.
    먼저 00111
        00100
        00101
        이렇게 3번이다. 
        작은 인덱스부터 하나씩 만들어간다고 생각하자! 
    '''
    cnt = 0
    for i in range(N):
        # i번에서 init과 obj가 서로 다르면 맞추기.
        if arr_init[i] != arr_obj[i]:
            for j in range(i, N):
                if arr_init[j] == 1:
                    arr_init[j] = 0
                else:
                    arr_init[j] = 1
            # print(arr_init)

            cnt += 1

    print(f'#{test_case} {cnt}')