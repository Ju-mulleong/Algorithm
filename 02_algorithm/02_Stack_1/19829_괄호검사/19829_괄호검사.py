import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def is_they_match():
    stack = []
    for i in text:
        if i == '(':    # 왼쪽 괄호만나면 push
            stack.append(i)

        elif i == ')':    # 오른쪽 괄호 만나면 pop 해서 비교 pop은 빈 스택인지 확인 !!!!!!!!!!
            if stack:   # 비어있지 않다면
                if stack.pop() != '(':  # 짝이 안맞으면
                    return 0
            else:   # 비어있다면
                return 0

    if stack:   # for i 다 돌았는데 stack이 남아있으면
        return 0

    return 1


for test_case in range(1, 1+T):
    text = input()
    # print(text)

    print(f'#{test_case} {is_they_match()}')