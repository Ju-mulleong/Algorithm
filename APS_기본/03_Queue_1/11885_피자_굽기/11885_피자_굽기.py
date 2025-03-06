import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def find_pizza():
    while True:  # 피자가 하나 남을 때까지 반복
        k = 0
        while k <= len(oven):
            # print(oven)
            if k >= len(oven):  # 피자 꺼내서 오븐의 길이 변경됬으면
                break
            oven[k][1] = oven[k][1] // 2
            if oven[k][1] == 0:  # 치즈가 다 녹으면
                if pn_list:  # 남은 피자가 있으면, 이 자리에 넣기
                    oven[k] = pn_list.pop(0)
                else:  # 남은 피자 없으면 꺼내기만 하기
                    oven.pop(k)
                    # 남은 피자없으면 오븐 길이 변경된다,
                    # 자연스럽게 한 칸 땡겨진다.
                    # 여기서 뺀 인덱스에서 다시 시작해야함.
                    # 즉, while문 맨 밑에 k+=1 하면 안된다.
                    # 하지만 len(oven)가 1이되면 빠져나가야함.
                    if len(oven) == 1:
                        return
                    continue

            k += 1
        # print(oven)


for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 화덕의 크기, M은 피자의 개수

    c_lst = list(map(int, input().split()))
    # M개의 피자에 뿌려진 치즈의 양의 리스트 c_lst

    pn_list = [[0, 0] for _ in range(M)]

    for i in range(1, M+1):     # 피자 번호매기기
        pn_list[i-1] = [i, c_lst[i-1]]

    # print(c_lst)
    '''
    Queue로 확인? ㄴㄴ
    피자 넣는걸 Q로 하자
    Queue로 확인하면 한번 확인하고, 그 다음번에 확인할때 한 바퀴 돌았다는 뜻이니까 C가 절반이 된다.
        확인하고, c = 0이 되면 다시 c_lst에서 피자 하나 더 넣기
        
    마지막까지 남아있는 피자 번호 알아내기
    10개 중에 4개 맞음
    
    '''

    # 화덕에 피자 넣기
    oven = pn_list[:N:]
    # print(oven)

    # 남은 피자 리스트
    if N == M:
        pn_list = []
    else:
        pn_list = pn_list[N::]
    # print(pn_list)

    find_pizza()

    # 피자 모두 구운 뒤, oven에 남아있는 번호 출력
    print(f'#{test_case} {oven[0][0]}')


