import sys
sys.stdin = open('input.txt', 'r')

# 이 문제는 더하기만해서 후위표기로 안 바꿔도 됨
# 후위표기는 내일 제대로 해보고 오늘은 일단 greedy로 해보자


T = 10


for test_case in range(1, 1+T):
    len_expr = int(input())     # expr의 길이 주어짐
    expr = list(input())
    # print(expr)

    stack = [0] * len_expr      # 연산자 스택
    expr_after = []

    for i in range(len(expr)):

        expr_after += expr[i]

        if i == 1:
            continue

    expr_after += '+'

    for i in range(len(expr_after)):
        if i == '+':






