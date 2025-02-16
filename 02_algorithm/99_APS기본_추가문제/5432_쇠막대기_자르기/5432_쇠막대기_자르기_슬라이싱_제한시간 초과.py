import sys
sys.stdin = open('input.txt', 'r')

'''
결국 '(' 다음에 바로 ')' 가 나오면 그건 레이저, 그렇지 않으면 쇠막대기
각 쇠막대기의 시작점을 기억하고 있다가, 쇠막대기의 끝이 나오면 
그 시작~끝 안에 있는 레이저의 수 +1이 잘라진 쇠막대기의 수

stack 사용
    stack안에 stack?

1. 그냥 전체 input 2번 순회
    첫 순회때 '(' 다음에 바로 ')' 나오면 둘 다 없애고 그 자리에 'R' 넣기.
    두 번째 순회 때 stack으로 하나씩 push하다가 ')' 나오면
        다시 하나씩 peek한다. '(' 나올때까지.
        '(' 나오면 이거 pop한다. 이때까지 peek한것중 R의 개수 +1을 cnt에 더한다.

근데 이 방법은 시간 너무너무 오래걸릴듯


2. 한 번만 순회 
    pop하지 말고, 조건문을 하나 더 걸어서 찾자
    아니다 이것도 복잡하다 그냥 찾은 막대 첫단은 다른문자로 바꿔버리자    

이것도 오래걸린다고?

3. 재귀?
    재귀가 더 오래걸리지 않나
    
4. 이거 그냥 stack 만들지말고 검사만 하자.
    for i로 lst 순회하다가 

'''
T = int(input())

for test_case in range(1, 1+T):

    lst = list(input())
    N = len(lst)
    # print(lst)
    check = []
    cnt = 0
    i = 0
    while i <= N-1:
        if lst[i] == '(':
            if lst[i+1] == ')':
                lst[i] = 'R'
                lst[i+1] = 'R'
                i += 2
                continue
            elif lst[i+1] == '(':
                check.append(i)     # 쇠막대기의 시작단을 check에 append한다.
        elif lst[i] == ')':     # 쇠막대기 끝단이면
            cnt += ((lst[check.pop():i+1].count('R')) // 2) + 1
            # 가장 최근에 check에 append한 쇠막대기의 시작단과 끝단을 슬라이싱하여, 그 사이의 R을 카운트.
            # R/2가 레이저의 수이다.
            # 레이저의 수 +1 이 잘라진 쇠막대기의 수다.

        i += 1

    print(f'#{test_case} {cnt}')