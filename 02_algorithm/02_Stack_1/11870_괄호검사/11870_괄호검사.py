import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 이번엔 append, pop 안 쓰고 해보자
for test_case in range(1, 1+T):
    text = input()

    top = -1    # stack의 top 설정

    # 왼 괄호일때만 push 하면 된다. 문자나 기타 다른 기호는 무시
    stack = [0]*len(text)
    ans = 1
    for i in text:

        if i in '{(':   # 이건 pythonic한 방법. 일반적인 방법은 or 사용
            top += 1
            stack[top] = i

        elif i == ')':
            if stack:
                top -= 1
                if stack[top+1] != '(':
                    ans = 0

        elif i == '}':
            if stack:
                top -= 1
                if stack[top+1] != '{':
                    ans = 0

    if top != -1:
        ans = 0

    print(f'#{test_case} {ans}')