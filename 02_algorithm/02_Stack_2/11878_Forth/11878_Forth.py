import sys
sys.stdin = open('input.txt', 'r')

# Error
# 토큰이 연산자인데 남은 피연산자가 2개 미만 or 3개 이상 or 0개
# 이때 말고는..?
# 마지막인데 토큰이 피연산자
# 괄호는 없는듯?


def calculate():
    expr = list(input().split())    # expr로 후위연산식을 받는다.
    stack = []

    for i in range(len(expr)):
        if expr[i] not in '+-*/.':  # 피연산자라면
            stack.append(int(expr[i]))  # push

        else:  # 연산자이거나 '.'이라면
            if expr[i] == '.':
                if len(stack) >= 2:     # '.'나오면 stack길이 1이여야함.
                    return 'error'
                else:
                    return int(stack.pop())

            if len(stack) < 2:   # 연산자인데 stack의 남은 길이가 2미만이면
                return 'error'

            B = stack.pop()  # 먼저 pop한 stack을 연산자의 오른쪽으로 사용
            A = stack.pop()

            if expr[i] == '+':
                stack.append(A + B)     # 계산 결과 stack에 push

            if expr[i] == '-':
                stack.append(A - B)     # 계산 결과 stack에 push

            if expr[i] == '*':
                stack.append(A * B)     # 계산 결과 stack에 push

            if expr[i] == '/':
                stack.append(A / B)     # 계산 결과 stack에 push


T = int(input())

for test_case in range(1, 1+T):

    print(f'#{test_case} {calculate()}')



