import sys
import pprint
sys.stdin = open('input.txt', 'r')


'''
1. 미생물 수와 위치, 이동방향이 주어짐
2. 맨 끝 셀에 도달하면(약품이 칠해진 셀), 수가 절반으로줄고(나머지 버림) 이동 방향이 "반대로 바뀜"
3. 이동했을때, 두 군집이 같은 위치에 도착한다면, 미생물 수는 합쳐지고 방향은 합치기전 다수쪽의 방향을 따라감.
    (합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않음)
M시간 후 남아있는 미생물 "수"의 총합 구하기
'''


# 미생물 이동
def move():
    global micro_lst
    di = [0, -1, 1, 0, 0]      # 더미, 상, 하, 좌, 우 순서대로
    dj = [0, 0, 0, -1, 1]

    for micro in micro_lst:
        if micro == [0]:    # 병합된 미생물 자리 넘기기
            continue

        # print(micro)
        d = micro[3]    # micro의 인덱스 3이 방향이다.
        i = micro[0]
        j = micro[1]

        ni = i + di[d]
        nj = j + dj[d]

        # 일반 델타응용과는 다르게 무조건 정상인덱스이다. 초기조건에 약 바른 셀에는 미생물 없고, 경계에 다다르면 방향 바꾸므로.
        # micro의 위치 이동
        micro[0] = ni
        micro[1] = nj

        if ni in (0, N-1) or nj in (0, N-1):    # 만약 도착지점이 약 바른 끝 셀이라면,
            # 미생물 수 절반되고,
            micro[2] //= 2
            # d가 홀수면(1,3) 1 더하고, 짝수면(2,4) 1 빼기
            if d % 2 == 0:
                d -= 1
            else:
                d += 1

            micro[3] = d    # d(방향) 반대로 바꾸기

    merge_micro()


# 겹치는 미생물 병합
def merge_micro():
    global K

    # 미생물 전부 이동했을 때, 좌표가 겹치는 미생물들이 있으면, 개수 합치고 제일 많은 미생물의 방향으로 방향 설정
    for i in range(K):
        if micro_lst[i] == [0]:    # 병합된 미생물 자리 넘기기
            continue

        # 기준 미생물 미생물 수, 방향 저장
        amount_lst = [micro_lst[i][2]]     # 미생물 수 저장
        direction_lst = [micro_lst[i][3]]   # 미생물 방향 저장
        for j in range(i+1, K):
            if micro_lst[j] == [0]:  # 병합된 미생물 자리 넘기기
                continue

            if (micro_lst[i][0], micro_lst[i][1]) == (micro_lst[j][0], micro_lst[j][1]):    # 만약 좌표 같은 미생물 있으면
                amount_lst.append(micro_lst[j][2])         # 미생물 수 저장
                direction_lst.append(micro_lst[j][3])       # 미생물 방향 저장

                # 어차피 병합되니까, 비교할 미생물 리스트에서 없애기(pop보다 그냥 0으로 바꾸는게 시간복잡도 측면에서 나을듯?)
                micro_lst[j] = [0]

                # 가지치기
                if len(amount_lst) == 4:
                    break

        # amount_lst 안의 미생물 수 비교
        # 초기 설정
        max_idx = 0
        max_v = amount_lst[0]
        sum_v = amount_lst[0]
        for m in range(1, len(amount_lst)):
            sum_v += amount_lst[m]
            if amount_lst[m] > max_v:
                max_v = amount_lst[m]
                max_idx = m

        # 병합된 미생물의 정보로 micro_lst 바꾸기
        micro_lst[i] = [micro_lst[i][0], micro_lst[i][1], sum_v, direction_lst[max_idx]]


T = int(input())

for test_case in range(1, 1+T):
    N, M, K = map(int, input().split())
    # N*N 개수의 정사각형 셀, M은 격리시간, K는 미생물 군집의 개수

    arr = [[0]*N for _ in range(N)]
    # print(arr)
    # 미생물 위치, 수, 이동방향 받기(상:1, 하:2, 좌:3, 우:4)

    micro_lst = [[0]*4 for _ in range(K)]
    # print(micro_lst)
    for k in range(K):
        micro_lst[k] = list(map(int, input().split()))

    # pprint.pprint(micro_lst)

    # 격리 시작
    # M시간동안(1시간에 1번 움직임)
    for _ in range(M):
        move()

    # M시간 후 미생물 총 합 계산
    sum_vv = 0
    for t in range(K):
        if micro_lst[t] != [0]:
            sum_vv += micro_lst[t][2]

    print(f'#{test_case} {sum_vv}')

