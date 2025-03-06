import sys
sys.stdin = open('input.txt', 'r')

T = 10  # test_case의 개수 T

for test_case in range(1, 1+T):
    Dump = int(input())     # 덤프 가능 횟수
    heights = list(map(int, input().split()))   # 상자들의 높이

    # 모든 덤프 진행 완료 후, 최고점과 최저점의 높이 차이 출력
    # 주어진 덤프 횟수 이내 평탄화 완료된다면, 그 때의 최고점과 최저점의 높이 차 반환

    # 단순하게 생각하면 가장 높은 height 중 하나 -1한 수 할당
    # 가장 낮은 height 중 하나에 +1한 수 할당
    # 이 작업을 for로 덤프횟수만큼 반복.
    # 가장 높은 height과 가장 낮은 height을 반복마다 찾아야 함.
    # 그리고 시행마다 최고점과 최저점의 차 구해서 0 또는 1되면 시행 종료하고 그 수 반환
    # 시행마다 최고점과 최저점 찾기?
    # 일단 시행마다 찾아보자.

    ''' 
    아니면 상자 수를 주니까 모든 상자의 합을 더하고 100(가로길이 100으로 고정)으로 나눈다
    만약 정수라면, 최고-최저 = 0.
    만약 실수라면(나머지가 있다면) 최고-최저 = 1
    몫은 평탄화 후의 높이(최고점)가 된다.
    이 때의 모양은 덤핑 횟수를 모두 썼을 때 모양.
    그리고 이 모양이 되기 위해 필요한 횟수(=p)는 '원래 모양에서 평탄화 후 최고점보다 높은 상자들의 합이다.'
    p와 주어진 Dump의 차이를 구하면 
    
    너무 복잡하다 처음 생각대로 하자

    '''

    max_height = heights[0]
    max_index = 0
    min_height = heights[0]
    min_index = 0
    for d in range(Dump):
        # 매 시행마다 최저/최고점 구하기
        for i in range(len(heights)):
            if heights[i] > max_height:
                max_height = heights[i]
                max_index = i
            if heights[i] < min_height:
                min_height = heights[i]
                min_index = i

        # 최고점에서 최저점으로 덤프하기
        heights[max_index] -= 1
        heights[min_index] += 1

        # 다시 최고/최저 구하기
        # 이 부분때문에 실행시간 오래걸리는 것 같음
        max_height = heights[0]
        max_index = 0
        min_height = heights[0]
        min_index = 0
        for i in range(len(heights)):
            if heights[i] > max_height:
                max_height = heights[i]
                max_index = i
            if heights[i] < min_height:
                min_height = heights[i]
                min_index = i

        # 이 때의 최고점 - 최저점 구하기
        # 만약 diff가 0 또는 1이라면 diff 반환
        diff = max_height - min_height
        if diff == 0 or diff == 1:
            break

    ans = diff

    print(f'#{test_case} {ans}')





