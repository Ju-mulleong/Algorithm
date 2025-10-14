from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
d = deque()
result = []

for i in range(N):
    command = input().split()
    length_c = len(command)
    length_d = len(d)
    com = command[0]

    if com == 'push_front':
        d.appendleft(command[1])
    elif com == 'push_back':
        d.append(command[1])
    elif com == 'pop_front':
        result.append(d.popleft() if d else -1)
    elif com == 'pop_back':
        result.append(d.pop() if d else -1)
    elif com == 'size':
        result.append(len(d))
    elif com == 'empty':
        result.append(0 if d else 1)
    elif com == 'front':
        result.append(d[0] if d else -1)
    elif com == 'back':
        result.append(d[-1] if d else -1)
    
print(*result, sep='\n')    
