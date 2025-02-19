# 큐 생성
queue = [0] * 3
front = rear = -1   # 처음에는 -1로 front, rear 초기화

'''
enqueue도 front를 먼저 +1하고 원소를 빼는거고, 
dequeue도 rear를 먼저 +1하고 원소를 더한다.
'''


# 1, 2, 3 인큐
rear += 1           # enqueue 1
queue[rear] = 1

rear += 1           # enqueue 2
queue[rear] = 2

rear += 1           # enqueue 3
queue[rear] = 3


while front != rear:    # 큐에 원소가 남아있으면, 워소가 비었다면 front == rear이 된다.
    front += 1
    t = queue[front]
    print(t)


# # 1 디큐
# front += 1
# print(queue[front])   # dequeue 1

q = []
# enqueue 1
q.append(1)     # enqueue 1
print(q)
q.append(2)     # enqueue 2
print(q)
q.append(3)     # enqueue 3
print(q)

print(q.pop(0))     # dequeue 1
print(q)
print(q.pop(0))     # dequeue 2
print(q)
print(q.pop(0))     # dequeue 3
print(q)

'''
보이기는 간단해 보이지만, 실제로 append(), pop()은 굉장히 동작속도가 느리다!!!
'''























