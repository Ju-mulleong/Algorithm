import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T
arr_paper = []

for test_case in range(1, 1+T):
    dj, di = map(int, input().split())  # dj는 도화지의 왼쪽 변과의 거리, di는 아래쪽 변과의 거리

    N = 10
    # 색종이의 크기는 10 * 10 이다.

    '''
    이거 좌표계처럼 0,0 으로 생각해야 편할듯
    dj = 3, di = 7를 받았을 때 색종이의 크기는
        [   [3, 7], [3, 8] ... [3,17]
            [4, 7]
            .
            .
            .
            [13, 7] ...     [13, 17]
        ]
    결국 넓이만 구하면 된다. 
    순서 상관 없
    
    for로 색종이 마다 좌표를 원소로 가진 배열로 만든다.
    색종이 넓이를 계속 넓힐까? 이미 있는 원소 넣으려고 하면 skip 하고
    색종이 수 만큼 반복한 다음에 그 list의 길이가 검은 영역 넓이다.
    '''


    for j in range(N):
        for i in range(N):
            if [j + dj, i + di] in arr_paper:
                continue
            arr_paper.append([j + dj, i + di])

print(len(arr_paper))

# 답은 나왔는데 시간 말도 안되게 오래 걸림
