import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    tc = int(input())

    password = list(map(int, input().split()))

    my_deque = deque(password)

    '''
    password는 8자리로 고정.
    첫번째 숫자를 1 감소한 후 dequeue 하고 그대로 enqueue
    두번째 숫자를 2 감소한 후 dequeue 하고 그대로 enqueue ...
    
    다섯 번째 숫자를 5 감소한 후 dequeue 하고 그대로 enqueue
    여기까지가 한 사이클
    
    숫자에 0 은 안주는듯?
    이렇게 무한반복하다가 숫자가 0보다 작아지면 0으로 저장하고, 그 때 이 숫자배열이 암호가 됨.
    deque 쓸까?
    
    '''

    dec_num = 1
    while dec_num:
        for i in range(1, 6):
            # queue 맨 앞 숫자 dequeue
            num = my_deque.popleft()
            # i만큼 감소시키고 enqueue
            dec_num = num - i

            # 이때 num -i 가 0 이하가 될 경우, 0으로 저장하고 반복 종료
            if dec_num <= 0:
                dec_num = 0
                my_deque.append(dec_num)
                break

            my_deque.append(dec_num)

    ans = list(map(str, my_deque))

    print(f'#{tc} {" ".join(ans)}')
