import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 한 줄, 세로 한 줄로 도로 건설시 최소비용, 최소비용일 때 높이 구해서 출력
    # 최소 비용이 같은 경우가 둘 이상일 때는 낮은 높이로 도로를 건설한다.
    '''
    이차원배열 행 우선탐색으로 훑기
    각각 델타로 가로로 전부, 세로로 전부 훑음
    현재 값과 발견한 값과의 차를 구해서 각 시행마다 합산한다.
    시행마다 합산값과 (탐색값 중 최댓값) 기억해야함
    시행마다 합산값 최소이면 합산값, (탐색값 중 최댓값) 업데이트
    
    만약 시행 후 합산값과 최솟값 같으면, (탐색값 중 최댓값)을 비교하여 낮은 쪽을 기억한다.
    '''
    # 높이를 낮춰서 지을수도 있다

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    min_cost = 5 * (2*N-1)      # 적당히 큰 수

    for i in range(N):
        for j in range(N):
            sum_v = arr[i][j]
            cnt = 0
            dict_h = {1:0, 2:0, 3:0, 4:0, 5:0}      # 높이는 1이상 5이하
            dict_h[arr[i][j]] = 1   # 현재 기준값도 딕셔너리에 추가
            for d in range(4 * N):   # 최악의 경우 N바퀴 돌아야함, 4*N번 시행
                k = 1 + d//4
                d = d % 4

                ni = i + di[d] * k
                nj = j + dj[d] * k

                if 0 <= ni <= N-1 and 0 <= nj <= N-1:   # 정상인덱스라면
                    '''
                    높이를 어디에 맞출 것인가?
                        이번 시행의 평균 높이 구하면 될듯.
                        평균높이에 좀 더 가까운 정수로 맞추자.
                        만약 소수점이 0.5라면 낮은 높이를 찾는 문제니까 반내림하자 
                        
                    아니다 이거 소수계산하는것보다 그냥 모든 경우의수 계산해서 구하는게 낫겠다
                    그냥 값들을 전부 dict에 저장하는게 이후 계산에 편할듯?
                    dict 키를 높이로 / 값을 그 높이칸의 개수로
                    시행 끝났는데 키 2개면 높이 결정 작은 수
                    '''
                    dict_h[arr[ni][nj]] += 1    # dict_h 안에 키-값 할당


                    cnt += 1
                    if cnt == 2*N-2:    # 도로 높이 구하는 횟수 정해져있음, 2N-2번 구함.(자기 자신은 계산 안하는데 2N안에 자기자신이 2번들어가니까)
                        break


            # 방향 탐색 전부 끝나면 비용 경우의 수 구하기
            # print(dict_h)
            # 모든 칸의 합 구하기

            for p in dict_h.keys():         # 도로 높이를 1,2,3,4,5라고 가정하고 비교
                sum_of_cost = 0
                for h in dict_h.keys():
                    sum_of_cost += abs((p - h)* dict_h[h])
                # print('i', i, 'j', j, 'p', p, 'h', h,'sum_of_cost:',sum_of_cost)

                if sum_of_cost < min_cost:
                    min_cost = sum_of_cost
                    height = p             # 비용 최소일때의 높이 height

                elif sum_of_cost == min_cost:
                    if p < height:  # 지금 계산의 높이가 현재기준 최솟값일때 높이보다 작으면
                        height = p     # 더 작은 높이로


    print(f'#{test_case} {min_cost} {height}')



'''
for p in dict_h.keys():
    sum_v += p * dict_h[p]      # 높이 * 그 높이의 칸 수
    


#print(f'sum_v:',sum_v)

# 높이별 비용 구하기
for p in dict_h.keys():
    sum_of_cost = abs(sum_v - p * (2*N-1))
    # 도로의 높이를 1,2,3,4,5로 건설할때 각각 비교
    if sum_of_cost == 0:
        print(test_case,i,j,)

    #print('p', p)
    #print(f'sum_of_cost', sum_of_cost)

    # 높이별 비용 중 최솟값 구하기
    if sum_of_cost < min_cost:
        min_cost = sum_of_cost
        height = p             # 비용 최소일때의 높이 height

    elif sum_of_cost == min_cost:
        if p < height:  # 지금 계산의 높이가 현재기준 최솟값일때 높이보다 작으면
            height = p     # 더 작은 높이로



이렇게 구하면 

      1
3 2 3 2
      1
      2
      
처럼 2로 도로를 맞출때 비용을 0으로 계산한다.....


'''