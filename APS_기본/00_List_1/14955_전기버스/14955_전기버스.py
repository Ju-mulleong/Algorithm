import sys
sys.stdin = open("input.txt", 'r')

T = int(input())    # 테스트케이스의 개수 T

for test_case in range(1, 1+T):

    K, N, M = map(int, input().split())
    # K는 한 번 충전으로 최대한 이동할 수 있는 정류장 수
    # N은 0번에서 출발해서 종점인 정류장의 번호
    # M은 충전기가 설치된 정류장 수

    M_list = list(map(int, input().split()))
    # M_list는 충전기가 설치된 정류장 번호들의 list

    # print(K, N, M, M_list)

    # 일단 출발해서 K번 앞까지 검사하여 제일 먼 곳의 충전기에서 충전
    # 하나밖에 없으면 그거 충전
    # 언제나 충전한 위치에서 다시 시작
    # 충전 할 때마다 cnt += 1
    # N번에 도착하면
    # cnt 반환

    '''
    bus_stop = [0]*N
    이거 리스트 만들고 인덱스로 정류장이라고 생각.
    충전소 있는 인덱스는 값 = 1
    ex) [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    while로 '도착 할 때 까지' K만큼 앞까지 검사하는거 반복하고
    그 중에 1이 있는 인덱스 하나면 그거, 여러개면 인덱스 가장 높은 인덱스 에서 다시 출발
    만약 검사하다가 현재 인덱스 + K 보다 N이 작으면 도착했다는 뜻.     
    '''

    bus_stop = [0] * N

    for i in M_list:
        bus_stop[i] = 1

    # print(bus_stop)
    now_index = 0
    max_index = 0
    cnt = 0
    flag = 1
    while now_index + K < N:

        for i in range(1, K + 1):     # K개 검사, 제일 먼 충전기의 index = max_index
            if bus_stop[now_index+i] == 1:
                max_index = now_index + i
                # print(max_index)

            if i == K:     # 마지막 K 인덱스까지 완료하면  충전횟수 cnt +1, 현재 now_index를 max_index로 설정
                if max_index == now_index:  # 마지막 검사까지 했는데 max_index가 변하지 않았을때(충전기 설치를 잘못함)
                    cnt = 0
                    flag = 0
                else:
                    cnt += 1
                    now_index = max_index

        if flag == 0:   # flag가 내려가면 while문 빠져나가기
            break

        # print(now_index, cnt)

        # print(now_index + K, N)

    print(f'#{test_case} {cnt}')