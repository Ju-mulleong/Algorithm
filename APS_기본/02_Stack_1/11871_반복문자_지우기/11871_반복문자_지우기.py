import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    text = input()

    # 중복문자를 지운 후 남은 문자열의 길이 출력
    # 문자열 자체를 stack으로 만들자
    '''    
    stack형식으로 for i로 하나하나 push하고
    만약 이번 i가 top과 같으면 pop한다.(push 안함)
    
    '''

    top = -1
    stack = [0]*len(text)

    for i in text:
        if top > -1:       # pop 하기 전 확인
            if i == stack[top]:
                top -= 1
                stack[top+1] = 0    # pop하기.
                continue

        # 기본적으로 push
        top += 1
        stack[top] = i

    # stack에서 0 지우기
    cnt = 0
    for i in stack:
        if i != 0:
            cnt += 1

    print(f'#{test_case} {cnt}')

'''
문제에서 만약 문자열에 0이포함되있으면 안 된다.
또 stack을 text의 길이와 같은 길이로 만드는 것보다
그냥 빈 list로 만들고 append, pop 하는게 더 자연스러운듯?
그러면 stack에서 0 지우는 과정 안해도 된다.
'''