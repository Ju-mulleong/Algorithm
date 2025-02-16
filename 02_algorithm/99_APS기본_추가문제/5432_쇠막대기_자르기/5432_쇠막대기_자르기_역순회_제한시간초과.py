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

    
'''
T = int(input())

for test_case in range(1, 1+T):

    lst = list(input())
    N = len(lst)
    # print(lst)
    stack = []
    cutted_stick = 0
    i = 0
    while i <= N-1:
        # stack 시작
        if lst[i] == '(':   # i == N-1일때. 즉 리스트의 끝 인덱스일때 '('일수는 없다.
            if lst[i+1] == ')':     # 레이저면 stack에 'R' push하고 인덱스 하나 건너뛰기
                stack.append('R')
                i += 2
                continue
            else:
                stack.append('(')   # 레이저 아니면 stack에 '(' push하기.

                # 이 인덱스 check에 기억해두기

        elif lst[i] == ')':     # 쇠막대기 끝단 나오면
            cnt_R = 0
            cnt = 0
            for j in range(len(stack)-1, -1, -1):     # stack 거꾸로 순회
                if stack[j] == 'R':
                    cnt_R += 1
                elif stack[j] == '(':   # 거꾸로 순회하다가 '('만나면
                    stack[j] = '!'      # 다음 반복때 안걸리도록 !으로 바꾸기
                    cutted_stick += cnt_R + 1    # 자른 막대수 저장
                    break       # for j 종료

        i += 1


    print(f'#{test_case} {cutted_stick}')