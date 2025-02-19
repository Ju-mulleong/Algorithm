import sys
sys.stdin = open('input.txt', 'r')


def is_empty():
    return front == rear
    # front와 rear이 같으면 Q가 비었다는 것
    # 비었으면 True 반환


def is_full():

    return (rear+1) % len(circular_Q) == front
    # rear+1 즉 다음 enQueue를 하기 위한 위치가 front라면, Queue가 꽉 찼다는 것
    # 꽉 찼으면 True 반환


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # 숫자의 개수 N, 맨 앞의 숫자를 맨 뒤로 보내는 작업의 횟수 M
    # 작업은 결국 deQueue한 뒤 그 원소를 그대로 enQueue 하는 것

    # 원형 큐?
    circular_Q = [0]
    circular_Q.extend(list(map(int, input().split())))
    # 원형 큐는 front 비어놔야함.
    # print(circular_Q)

    front = 0
    rear = len(circular_Q)      # 이미 Queue 다 차있으니까

    for i in range(M):  # 작업 M번 반복
        # deQueue 하기.
        if not is_empty():  # 비어있지 않을때만 작업
            front = (front+1) % len(circular_Q)
            element = circular_Q[front]

        # enQueue 하기.
        if not is_full():   # 꽉 차 있지 않을때만 작업
            rear = (rear+1) % len(circular_Q)
            circular_Q[rear] = element

    # 모든 작업 끝난 후, 맨 앞의 숫자 출력
    # 맨 앞의 숫자니까 비어있는 프론트보다 한 스텝 더 가야한다 (front+1)%len(circular_Q)
    print(f'#{test_case} {circular_Q[(front+1) % len(circular_Q)]}')

