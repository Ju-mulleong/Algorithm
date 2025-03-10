import sys
sys.stdin = open('input.txt', 'r')


'''
최단시간이니까 dfs?
겹치지 않는 한, 한 단위시간에 여러명 이동하니까 BFS
이동하는데는 거리에 관계없이 단위시간이 걸린다
방 400개
" 이동경로가 겹치면 한 사람은 기다렸다가 다음 차례에 이동해야한다"
    = 겹칠때마다 단위시간 +1
홀수방은 위, 짝수방은 아래이다.
그냥 출발~도착의 경로가 겹치면 겹치는 것
그냥 항상 작은쪽에서 출발한다고 생각해도됨. 어차피 이동하는것이 중점이니까

실제로 이동하는 것처럼 생각해볼때,
    시간이 지날때마다 겹치던게 안 겹칠 수도 있다.
    3차원 배열?
'''

# 각 겹쳐진 경로마다 최소로 돌아가는 경우 찾기
def find_min(path_arr):
    for i in range(1, len(path_arr)):
        # 0인덱스를 제외한 값들 중에서 dfs로
        # 제외하고, 남은 인덱스들로 겹치는 지 확인
        #



T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 돌아가야 할 학생들의 수 N

    # 입력 하나씩 받고, 받을 때마다 겹치는지 확인
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start

    arr = [[[start, end], [start, end]]]    # 첫 경로 arr에 넣기
    cnt_lst = [1]
    for i in range(1, N):
        start, end = map(int, input().split())
        if start > end:         # 무조건 start가 end보다 작도록(한 방향으로 이동하도록)
            start, end = end, start

        # start나 end가 같은 열이면 이미 겹침
        # start나 end가 짝수라면 arr[j][0]+1 이면 같은 열에서 start, 홀수라면 arr[j][n]-1
        same_column = []
        for now_position in (start, end):
            if now_position % 2 == 0:  # 짝수라면
                same_column.append(now_position - 1)
            else:  # 홀수라면
                same_column.append(now_position + 1)

        # print(same_column)

        flag = 0
        for j in range(len(arr)):
            # 출발점이나 도착점이 같은 열인지 확인, 같은 열이면 겹친다
            for k in arr[j][0]:
                if k in same_column:
                    flag = 1
                    break

            # start와 end가 둘 다 이미 생긴 경로의 시작점보다 작거나, 둘 다 이미 생긴 경로의 도착점보다 큰 경우 아니면 전부 겹친다
            # start나 end가 이 경로의 출발점, 끝점과 같은 열이면 겹친다.
            if (start < arr[j][0][0] and end < arr[j][0][0]) or (start > arr[j][0][1] and end > arr[j][0][1]) and flag == 0:
                continue

            else:
                # cnt_lst[j] += 1        # 단위시간 증가
                # 경로 겹친거 적용해서 늘리기
                arr[j][0][0] = min(arr[j][0], start)
                arr[j][0][1] = max(arr[j][1], end)
                arr[j].append([start, end])
                break
        # 이미 생긴 경로 안에 아무것도 안 겹치면, 이 경로를 arr에 추가
        else:
            arr.append([[start, end], [start, end]])
            # cnt_lst.extend([1])
        # print(arr)
    # print(cnt_lst)

    min_v = 0
    for path_arr in arr:
        temp_min = find_min(path_arr)
        min_v = max(min_v, temp_min)


    cnt = max(cnt_lst)  # 각 경로중 단위시간이 가장 오래걸리는게 필요한 시간
    print(f'#{test_case} {cnt}')


