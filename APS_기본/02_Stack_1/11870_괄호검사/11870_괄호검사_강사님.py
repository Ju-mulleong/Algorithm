import sys
sys.stdin = open('input.txt', 'r')

def solve(text):
    stack = []
    # text 문자열을 문자별로 스캔
    for ch in text:
        # 1. 왼쪽괄호: push
        if ch == '(' or ch == '{':
            stack.append(ch)
        # 2. 오른쪽 괄호: pop
        elif ch == ')' or ch == '}':
            # 2.1 : isEmpty
            if len(stack) == 0:
                return 0
            # 2.2 : 짝검사
            else:   # else안써도 상관없다.
                temp = stack.pop()
                if ch == ')' and temp != '(':
                    return 0
                elif ch == '}' and temp != '{':
                    return 0

    # 3. 스택이 isEmpty인지 확인
    if stack:
        return 0

    return 1


T = int(input())
for test_case in range(1, 1+T):

    text = input()

    print(f'#{test_case} {solve(text)}')
