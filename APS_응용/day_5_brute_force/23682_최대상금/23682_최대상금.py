import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(lst, cnt):
    global max_v, memo
    lst_str = ''.join(lst)
    # print(lst_str)

    # 종료조건
    if cnt == t:
        # 최댓값 업데이트
        max_v = max(max_v, int(lst_str))
        return

    # 가지치기 - 메모이제이션 활용
    if (lst_str, cnt) in memo:
        return  # 같은 숫자 조합 + 같은 남은 횟수를 이미 방문했다면 탐색 중단

    memo.add((lst_str, cnt))    # 새로운 경우라면 저장

    # 자리 교환
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            dfs(lst, cnt+1)
            lst[i], lst[j] = lst[j], lst[i]   # 원복


for test_case in range(1, 1+T):
    t_str, t = input().split()
    t = int(t)
    lst = list(t_str)
    max_v = 0

    memo = set()

    dfs(lst, 0)

    print(f'#{test_case} {max_v}')

'''
# 가지치기 1
    # 횟수가 무제한이라고 생각할 때 최대인 카드 조합을 이미 완성했는데,
    # 1. 같은 숫자 2개이상 있다.
    #       남은 교환횟수에 상관없이 그것끼리 계속 바꾸면 된다.
    # 2. 같은 숫자가 없다.
    #       남은 교환횟수가 짝수라면 아무거나 바꿨다가 다시 역으로 돌아오면 되니까 최댓값 가능.
    #       남은 교환횟수가 홀수라면 불가능. 가지치기 불가
    if flag == 0:
        lst_str = ''.join(lst)
        now_num = int(lst_str)

        if now_num == int(temp_str):    # 현재 카드 조합이 이론상 최대 카드 조합일 때
            # 1. 서로 같은 숫자가 존재한다.
            if len(lst) > len(set(lst)):    # 중복이 존재한다면(같은숫자가 존재한다면) 중복 제거시 길이 짧아짐
                max_v = int(temp_str)
                flag = 1
                return              # 함수 끝내기

            # 2. 같은 숫자가 존재하지 않으면,
            else:
                if (t - cnt) % 2 == 0:      # 남은 교환횟수 짝수라면 함수 끝내기
                    max_v = int(temp_str)
                    flag = 1
                    return
시도해본 가지치기기
'''