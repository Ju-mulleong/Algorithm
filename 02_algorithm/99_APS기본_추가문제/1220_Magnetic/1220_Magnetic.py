import sys
import pprint
sys.stdin = open('input.txt', 'r')

'''
문제의 조건에 따른 '교착상태'의 개수를 구하는 것.
교착상태는 자기장을 걸었을때 서로 상극인 자성체들이 충돌하여 서로 움직이지 못하는 상태를 말한다.

열 우선 탐색으로 봐야할듯
    1은 N극, 2는 S극의 자성체를 의미한다.
    테이블 윗부분에 N극, 아랫부분에 S극이 위치한다.
    
    열 우선탐색으로 한 열마다 while?
    아니다 최대 N(=100)번 움직이니까 그냥 100으로 하자.
    조건 맞추면 continue하고
    전 시행과 이번 시행 후의 결과물이 같으면 교착?
    
    
    '교착상태'만 구하는 거니까 한 열에 1과 2가 동시에 있어야 한다.
    둘 중 하나만 있는 열이면 continue로 넘기기
    
    한 열에서 1은 아래로, 2는 위로 간다.
    한 번 for로 돌린다.
        1과 2 각각 진행 방향으로 다음 칸이 0 이라면
        1은 아래로 1칸, 2는 위로 1칸 간다
            만약 진행방향으로 진행 후 1의 인덱스가 99, 2의 인덱스가 0 이라면
            
    시행마다 모든 자성체가 교착상태인지 검사
        전 시행 후 열을 temp_list에 할당
        temp_list와 현재 시행 후 열을 비교
        교착상태 아니라면, 현재 시행 후 열을 다시 temp_list에 할당
        반복
    이 열이 교착상태라면, 다음 열로 넘어가서 다시 반복
    
    교착상태 개수 세기
        만약 모든 열이 교착상태라면, 
 
'''

'''
열 우선 탐색?, 

한 열에 1 기준으로 아래 방향으로 처음 만나는 2가 존재하고, 이 사이에  1이 없으면
    이 1과 2는 교착이 된다.
    다음 1의 인덱스 찾기
    만약, 1 기준으로 2가 아래 인덱스에 있는데 그 사이에 1이 있다면, 어차피 하나의 교착이므로 
        pass

아니다 그냥 1 기준으로 한 열에서 먼저 생각해보자


'''


T = 10

for test_case in range(1, 1+T):
    N = int(input())     # 이 값은 항상 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 100*100 2차원 배열 arr

    cnt = 0
    for i in range(100):
        flag = 0
        for j in range(100):
            if flag != 0:
                flag -= 1
                continue
            if arr[j][i] == 1:
                if j == 99:     # 아래로만 검사하니까 마지막에 도달하면 테이블 아래로 떨어짐
                    break
                for k in range(j+1, 100):
                    if arr[k][i] == 0:
                        continue
                    elif arr[k][i] == 1:
                        flag = k - j - 1    # 3 - 0 - 1
                        break
                    elif arr[k][i] == 2:
                        cnt += 1
                        break   # for k 빠져나감

    print(f'#{test_case} {cnt}')

