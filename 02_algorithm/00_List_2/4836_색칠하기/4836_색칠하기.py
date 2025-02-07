import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

# 10 x 10 격자
# 빨 + 파 = 보 되는 칸 수 구하기
# 같은 색인 영역은 겹치지 않는다.

for test_case in range(1, 1+T):

    N = int(input())    # 칠할 영역의 개수 N, 예를들어 2이면 (빨, 파) 3이면 (빨, 파, 파) 등

    # 왼쪽 위 모서리(r1, c1) 오른쪽 아래 모서리(r2, c2) 색깔 color
    # 주어진 input들을 사용하여 for문돌려서 2차원 배열 만든 뒤,
    # 같은 색깔의 list는 중복제거해서 합치고,
    # 빨 파 list의 원소(좌표)들 끼리 비교해서 같으면 cnt +=1
    # 일단 실행시간 신경쓰지말고 해보기

    # [0]*2 for _ in range(2)] [[0, 0], [0, 0]]

    # 중복제거 위해 set으로 설정
    red_coordinate = []
    blue_coordinate = []

    for i in range(N):
        temp_list = []
        r1, c1, r2, c2, color = list(map(int, input().split()))     # 각 변수에 할당

        for r in range(r2-r1+1):    # 색칠 영역의 가로길이   # 0, 1, 2
            for c in range(c2-c1+1):  # 색칠 영역의 세로 길이  # 0, 1, 2
                lst = [r1+r, c1+c]
                temp_list.append(lst)

        # print(temp_list)    # [[2,2], [2,3], [2,4]...]

        if color == 1:  # 만약 color가 red라면
            for a in temp_list:
                if a not in red_coordinate:
                    red_coordinate.append(a)

        if color == 2:  # 만약 color가 blue라면
            for a in temp_list:
                if a not in blue_coordinate:
                    blue_coordinate.append(a)

    # red_coordinate 와 blue_coordinate 비교해서 똑같은 원소있으면 cnt += 1
    # print(red_coordinate)
    # print(blue_coordinate)
    # cnt = 0
    # for i in red_coordinate:
    #     for j in blue_coordinate:
    #         if i == j:
    #             cnt += 1

    cnt = 0
    for i in red_coordinate:
        if i in blue_coordinate:
            cnt += 1

    print(f'#{test_case} {cnt}')