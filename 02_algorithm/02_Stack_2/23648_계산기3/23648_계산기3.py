import sys
sys.stdin = open('input.txt', 'r')

'''
1. 주어진 식을 후위 표기식으로 바꾼다.
2. 후위 표기식을 stack을 활용하여 계산한다.
'''

T = int(input())


# 중위 표기식을 후위 표기식으로
def fix_expr(expr):
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # in-coming-priority    들어올때 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # in-stack-priority     스택 안에서 우선순위
    expr_fixed = []
    global top
    global stack

    for token in expr:
        if token not in '(*/+-)':   # token이 피연산자면
            expr_fixed.append(token)

        elif token == ')':     # token이 닫는 괄호라면, 여는 괄호가 나올때가 전부 stack에서 pop하고, token은 버린다, 여는 괄호도 버린다.
            while stack[top] != '(':
                expr_fixed.append(stack[top])
                top -= 1
            top -= 1    # 여는괄호 버림

        else:      #
            if top == -1 or isp[stack[top]] < icp[token]:  # token이 연산자. top이 -1이거나 token의 우선순위가 더 높거나
                top += 1
                stack[top] = token
            elif isp[stack[top]] >= icp[token]:     # token의 우선순위가 stack[top]보다 작거나 같을 경우.
                while top > -1 and isp[stack[top]] >= icp[token]:
                    expr_fixed.append(stack[top])
                    top -= 1
                # while에서 빠져나오면, 즉 stack[top]의 우선순위가 토큰보다 낮아지면 push
                top += 1
                stack[top] = token

    print(expr_fixed)
    print(stack)
    return expr_fixed

    # 여기까지 끝나면, 자연스럽게 stack이 빈다.?



# 후위 표기식을 계산
def calculate_expr(expr_fixed):
    global top
    global stack
    for token in expr_fixed:
        if token not in '+-/*':     # token이 피연산자면 stack에 push
            top += 1
            stack[top] = int(token)
        else:   # token이 연산자면, stack에서 2개 pop한다.
            op2 = stack[top]    # pop()
            top -= 1
            op1 = stack[top]    # pop()
            top -= 1
            if token == '+':  # op1 + op2
                top += 1  # push()
                stack[top] = op1 + op2
            elif token == '-':
                top += 1
                stack[top] = op1 - op2
            elif token == '/':
                top += 1
                stack[top] = op1 / op2
            elif token == '*':
                top += 1
                stack[top] = op1 * op2

    return stack[top]


for test_case in range(1, 1+T):
    N = int(input())    # 식의 길이

    expr = list(input())    # 중위 표기식 expr
    # print(expr)

    stack = [0] * 100
    top = -1

    ans = calculate_expr(fix_expr(expr))      # calculate_expr(expr_fixed)

    print(f'#{test_case} {ans}')
    '''
    후위 표기식으로 바꾸기
        일단 중위표기식으로 input받기
        받은 중위표기식의 token을 for문으로 하나씩 본다.
            만약 token이 피연산자면 그대로 expr_fixed에 넣는다.
            elif, token이 연산자면 icp와 isp에 따라 달라진다.
                만약 top = -1이라면, stack이 비었으므로 연산자 그대로 추가
                또는 stack[top]의 우선순위(isp)와 비교해서 token(icp)이 더 높으면 그대로 push
                    즉, token이 여는괄호라면 무조건 push한다.
                token의 우선순위가 stack[top]보다 높지 않으면?
                    !!! token보다 낮은 우선순위가 나올때 까지 stack에서 하나씩 pop한다.
                    stack[top]이 token보다 우선순위 낮으면, 그때서야 push
                token이 닫는괄호라면
                    여는 괄호를 만날때까지 stack을 전부 pop하고 token은 버린다. 
    여기까지 하면 stack 빈다. 닫는괄호에서 전부 pop하기 때문에.
     
    후위 표기식을 계산
        후위 표기식을 for로 하나씩 본다.
        만약 피연산자면 후위 표기식에서 pop해서 stack에 push한다.
        
        
                         
    '''