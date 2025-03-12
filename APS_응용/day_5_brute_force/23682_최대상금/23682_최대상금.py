import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(i, lst, cnt, temp_str):
    global max_v, flag
    # 가지치기
    # 횟수가 무제한이라고 생각할 때 최대인 카드 조합을 이미 완성했는데,
    # 1. 같은 숫자 2개이상 있다.
    #       남은 교환횟수에 상관없이 그것끼리 계속 바꾸면 된다.
    # 2. 같은 숫자가 없다.
    #       남은 교환횟수가 짝수라면 아무거나 바꿨다가 다시 역으로 돌아오면 되니까 최댓값 가능.
    #       남은 교환횟수가 홀수라면 불가능. 가지치기 불가
    if flag == 0:
        now_num = int(''.join(lst))

        if now_num == int(temp_str):
            for pp in range(len(lst)):
                for kk in range(len(lst)):
                    if lst[pp] == lst[kk] or (t - cnt) % 2 == 0:
                        max_v = int(temp_str)
                        flag = 1
                        break
                    else:
                        continue


        # 종료조건
        if cnt > t:
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
    # temp_str은 교환 횟수가 무제한이라고 할 때 최대인 수

    for i in range(len(lst)):
        dfs(i, lst, 0, temp_str)

    print(f'#{test_case} {max_v}')