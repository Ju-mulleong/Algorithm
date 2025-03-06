import sys
sys.stdin = open('input.txt', 'r')

T = 10    # 테스트케이스의 개수는 10

for test_case in range(1, 1+T):
    N = int(input())    # 건물의 개수 N
    heights = list(map(int, input().split()))   # 빌딩 높이들의 리스트 heights
    sum_sunlight = 0    # 조망권 확보한 세대의 합

    # 좌우로 2칸이상 있을때 조망권이 확보됬다고 한다.
    # 조망권이 확보된 세대 수 구하기
    # 4 <= N <= 1000
    # 빈 칸도 N에 포함
    # 한 빌딩 기준 좌우로 2개의 빌딩만 비교하면된다.
    # 일단 좌우2개+자신 = 5개의 빌딩 기준 자신이 가장 높은 빌딩이어야 함.
        # 높이가 0 이면 바로 다음 빌딩으로
    # 그랬을때, 두 번째로 큰 빌딩의 높이만 빼주면 된다.
    flag = 0
    for i in range(2, N-2):
        if flag > 0:    # 이미 조망권이 확보된 수 나왔으면 그 뒤의 2개 인덱스 뛰어넘기 (조망권 나오면 flag=2 될것)
            flag -= 1
            continue

        if heights[i] == 0:     # 이번 칸이 빈 칸이면 continue
            continue

        # 그냥 제일 처음 생각했던 5개중 가운데가 최댓값인지 확인하고, 그 5개중에 2번째로 큰 높이 빼기.
        # 버블 정렬 2번만하면 된다.

        heights_list = []

        # i 기준으로 -2, -1, 0, +1, +2인 인덱스의 높이 리스트화
        for h in range(-2, 3, 1):
            heights_list.append(heights[i+h])

        for _ in range(2):  # 최댓값 + 그 다음 최댓값만 보면 되니까 최댓값 2번만 찾으면 된다.
            for j in range(4):  # 5개 중에서 2개씩 끊어서 비교하니까 4번 반복.
                if heights_list[j] > heights_list[j+1]:
                    heights_list[j], heights_list[j+1] = heights_list[j+1], heights_list[j]
        # print(heights_list)
        # heights_list = [n1, n2, n3, 2번째 최댓값, 최댓값]

        if heights_list[-1] == heights[i]:  # 최댓값이 i값이라면
            diff = heights_list[-1] - heights_list[-2]

            if diff > 0:
                sum_sunlight += diff
                flag = 2

    print(f'#{test_case} {sum_sunlight}')

    '''
    강사님 풀이
        for i in (2, N-2):
            max_v = 0
            for j in (5):
                if j != 2:
                    if max_v < arr[i - 2 + j]:
                        max_v = arr[i - 2 + j]
            if arr[i] > max_v:
                ans += arr[i] - max_v
        
        print(ans)
        
    '''

        # 이 아래는 전부 시도했다가 출력값 달랐던 것
        # heights[i]를 heights[i-2], heights[i-1], heights[i+1], heights[i+2]와 빼보기
        # 만약 그 수가 전부 양수라면, 그 중 가장 작은 수가 그 빌딩에서 조망권이 확보된 세대의 수.
        # 왼오 나눠서 해볼까
        # 그리고 조망권이 확보된 세대가 나왔다면, 그 뒤의 2칸은 조망권 x니까 continue.

        # num3 = 0
        # if heights[i] - heights[i-1] > 0:
        #     if heights[i] - heights[i-2] > 0:
        #         num1 = heights[i] - heights[i-2]
        #         if heights[i] - heights[i+1] > 0:
        #             if heights[i] - heights[i+2] > 0:
        #                 num2 = heights[i] - heights[i+2]
        #
        #                 if num1 > num2:     # 더 작은 수가 조망권이 확보된 수. 큰 수는 반대편이 조망권이 없다는 뜻이니까
        #                     num3 = num2
        #                 elif num1 < num2:
        #                     num3 = num1
        #                 elif num1 == num2:
        #                     num3 = num1
        #
        #                 sum_sunlight += num3
        #                 flag = 2            # num3 나오면 flag=2 할당
        # 근데 이렇게하면 생각해보니까 모든 경우에서 수를 저장하고 다 비교해야한다. 다시
        # 각 차를 요소로 가지는 list 만들고, 그 요소중 양수이고 가장 작은 수 찾기

        # diff_height = []
        # for j in range(-2, 3, 1):   # -2, -1, 0, 1, 2
        #     diff_height.append((heights[i] - heights[i+j]))
        #
        # switch = 1
        # min_diff = 0
        # for k in diff_height:
        #     if k > 0 and switch == 1:   # 처음으로 양수인 k 일단 최솟값으로 할당. # 그 후 비교하여 최솟값 업데이트
        #         min_diff = k
        #         switch = 0
        #         continue
        #     if 0 < k < min_diff:    # 양수이면서 min_diff보다 작으면 업데이트
        #         min_diff = k
        #     pass
        # if min_diff > 0 :
        #     if (diff_height[1] != 0 or diff_height[-2] != 0):
        #         # 이것도 틀림
        #         # 최솟값이 i+2라면 i와 i+1과의 차가 0인지 확인
        #         # 최솟값이 i-2라면 i와 i-1과의 차가 0인지 확인.  근데 이거 너무 번거로운 것 같으니까 다른 방법으로 풀자
        #         sum_sunlight += min_diff    # 만약 조망권이 확보된 세대가 있다면, sum_sunlight에 합산하고 다음 2블록 스킵
        #         flag = 2

        # 이렇게 하면 [i] - [i+1] = 0, [i] - [i+2] = 1 이면 조망권 확보가 없지만 이 식에서는 있다고 계산됨..

        # for height in heights:
        #
        #     for h in range(-1, 3, 1):  # -2, -1, 0, 1, 2
        #         heights[i] - heights[i+h]


