import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
'''
croak
crcoarkcoroakak
cr oa k   
  c  r  o      ak
       c r oak
3마리?
세 번째가 다시 첫번째 개구리의 울음소리 일수 있으므로 최소 2마리
개구리의 울음소리로 불가능한 경우 -1을 출력
'''
for test_case in range(1, 1+T):
    temp_str = input()
    shout = 'croak'

    # 만약 temp_str의 길이가 5의 배수가 아니면, 불가능
    if len(temp_str) % 5 != 0:
        print(f'#{test_case} -1')
        continue

    # 인덱스(개구리)별로 다음에 울어야 할 울음소리 인덱스
    frog_lst = [0]

    c = 0
    ans = 0
    while c < len(temp_str):
        for frog in range(len(frog_lst)):
            if temp_str[c] == shout[frog_lst[frog]]:
                # print('현재 개구리 울음')
                frog_lst[frog] += 1
                c += 1
                # 만약 croak 전부 다 울었으면, 최소로 해야하니까 초기화
                if frog_lst[frog] == 5:
                    frog_lst[frog] = 0
                # print(frog_lst)
                break
        # 현재 울음소리 진행중인 개구리가 아닐때(새로운 개구리 필요할 때)
        else:
            # 새로운 개구리는 항상 c부터 시작이고, 이미 c를 울었으니까 1
            # 만약 새로운 개구리 필요한데 c가 아니면 울음소리 불가능
            if temp_str[c] != 'c':
                ans = -1
                break
            else:
                frog_lst.append(1)
                c += 1
                # print(frog_lst)

    # 전부 끝나고, frog_lst가 모두 0이어야됨.
    if sum(frog_lst) != 0:
        ans = -1

    # 전부 끝난 뒤, frog_lst의 길이가 답
    if ans != -1:
        ans = len(frog_lst)

    print(f'#{test_case} {ans}')

