from collections import deque
import sys
input = sys.stdin.readline


"""
정수를 저장하는 큐를 구현 한 후, 입력으로 주어지는 명령을 처리
특별한 언급 없으면 deque같은거 써도 된다. 오히려 그걸 사용안하면 시간 안에 처리 못함.
"""

N = int(input())

q = deque()
for test_case in range(N):
    temp = input().split()
    command = temp[0]

    if command == "push" and temp[1]:  # 정수 X를 큐에 넣기
        q.append(temp[1])

    elif (
        command == "pop"
    ):  # 큐에서 가장 앞에 있는 정수를 제거하고, 출력, 큐가 비어있을 때는 -1 출력
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif command == "size":  # 큐에 들어있는 정수의 개수 출력
        print(len(q))

    elif command == "empty":  # 큐가 비어있으면 1, 아니면 0을 출력
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif (
        command == "front"
    ):  # 큐의 가장 앞에 있는 정수 출력, 큐가 비어있을 때는 -1 출력
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif command == "back":  # 큐의 가장 뒤에 있는 정수 출력, 큐가 비어있을 때는 -1 출력
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])

