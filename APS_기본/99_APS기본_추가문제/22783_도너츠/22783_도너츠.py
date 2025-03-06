import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

'''
그물로 점수 따보기
    그물은 총 (M-K + 1) * (N-K + 1)번 던진다.
    (M-K + 1) 번 만큼 같은 열에서 반복
    행 바꾸기 (총 (N-K + 1) 번) 만큼 행 바꿔야 됨.
    다시 (M-K + 1) 번 만큼 같은 열에서 반복
'''


def catch_fish(N, M, arr, K):    # now_row와 now_column 기본 값 0으로 설정
    # 그물 점수 계산식
    max_value = 0
    now_row = 0
    now_column = 0

    # now_row, now_column 은 그물 출발 기준점(가장 왼쪽 상단)의 인덱스

    for _ in range((M-K+1)*(N-K+1)):    # 그물 던지는 횟수는 정해져 있다.
        sum_value = 0

        # 인덱스 + 길이 == 길이라 좀 이상하긴한데 같을 때 조건확인하는거라 맞게 돌아간다.
        # 그림2처럼 첫 시행이면 이거 시작하자마자 now_row +1 증가시킨다..
        # 연못 크기가 K**2만 아니면 된다.
        # 물고기가 0인 경우는 없으니까 sum_value != 0으로 하자
        if N * M != K**2 and now_column + K > M:  # 그물이 행방향으로 끝까지 움직이면
            now_column = 0  # now_column 초기화 시키고 now_row += 1 (열방향으로 1칸 이동)
            now_row += 1

        # print(now_row, now_column)

        for i in range(K):      # 그물 한 번 던지기
            for j in range(K):
                if i == 0 or i == K - 1:  # 그물의 첫 행이나 끝 행일때
                    # print(arr[now_row + i][now_column + j])
                    sum_value += arr[now_row + i][now_column + j]

                elif j == 0 or j == K - 1:  # 그물의 첫 행이나 끝 행이 아니고, 첫 열이나 끝 열일 때  # 여기서 시간 너무 오래 썼다..
                    # print(arr[now_row + i][now_column + j])
                    sum_value += arr[now_row + i][now_column + j]

        print(sum_value)
        if sum_value > max_value:   # 최댓값 업데이트
            max_value = sum_value
            # print(max_value)

        now_column += 1  # 그물 한 번 잡을때 마다 행방향으로 1칸 움직이기

    # 그물이 열과 행 방향으로 끝까지 움직이면 종료
    return max_value


for test_case in range(1, 1 + T):
    N, M, K = map(int, input().split())  # 배열의 행의 개수 N, 열의 개수 M, 그물 한 변의 크기 K
    # print(N, M, K)

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 그물 모양만큼 경우의 수 내서 최댓값 구하기
    # 굳이 달팽이처럼 움직이려하지말고, K에 따라 값 구할수 있도록 해보자

    '''
    그물의 행은 K개, 행 우선 탐색으로 규칙 만들면
    0, K 번째 행은 전체 K개 열이 모두 점수다
    그 외의 행에서는 열에서 첫 값과 끝값만 점수다. 
    
    델타 똑바로 이해!!!!!!!!!!!!!!!!!!!
    시행마다 검사할 때 기준이 되는건 그냥 i,j 다. now+i, now+j가 아니다..
    '''

    print(f'#{test_case} {catch_fish(N, M, arr, K)}')











