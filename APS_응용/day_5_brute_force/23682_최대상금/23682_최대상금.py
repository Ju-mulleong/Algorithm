import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(i, lst, cnt, temp_str):
    global max_v, flag
    if flag == 0:
        # 가지치기
        # 만약, 현재 lst값이 이 카드들로 낼 수 있는 최댓값이라면, return, flag = 1
        if int(''.join(lst)) == int(temp_str):
            max_v = int(''.join(lst))
            flag = 1
            return

        # 종료조건
        elif cnt > t:
            # 최댓값과 비교
            if max_v < int(''.join(lst)):
                max_v = int(''.join(lst))
            return

        for ii in range(len(lst)):
            if ii != i:     # 값이 같은 서로 다른 위치 바꿔도 된다. 단, 자기자신을 바꾸는건 의미없으므로 제외
                lst[i], lst[ii] = lst[ii], lst[i]
                dfs(ii, lst, cnt+1, temp_str)
                lst[i], lst[ii] = lst[ii], lst[i]   # 원복


for test_case in range(1, 1+T):
    t_str, t = input().split()
    t = int(t)
    lst = list(t_str)
    int_lst = list(map(int, lst))
    max_v = 0
    flag = 0
    temp_str = ''
    sorted_lst = sorted(int_lst, reverse=True)
    for p in sorted_lst:
        temp_str = temp_str + str(p)
    # print(temp_str)

    for i in range(len(lst)):
        dfs(i, lst, 0, temp_str)

    print(f'#{test_case} {max_v}')