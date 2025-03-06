stack = []
for i in range(3):
    stack.append(i)
    print(stack)
    # 푸쉬


# !!! pop은 반드시 빈 배열인지 확인
while stack:    # stack이 비어있지 않다면
    print(stack.pop())