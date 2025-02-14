import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())


for test_case in range(1, 1+T):

    N = int(input())    # 지형의 개수(열의 길이) N
    if N == 0:
        print(f'#{test_case} {0}')
        continue

    arr = list(map(int, input().split()))
    if N == 1:
        print(f'#{test_case} {1}')
        continue
    elif N == 2:
        print(f'#{test_case} {1}')
        continue


    # 본인 기준 열 -1, 열 +1 의 값들과 비교하여 그 둘보다 크면 봉우리다.
    # 만약 시행했는데 봉우리일경우, 다음 열 봉우리 계산은 스킵(이미 자신보다 낮음)

    # 첫과 끝 인덱스 일 경우, 각각 오/왼만 비교하면됨.
    # N이 1일때랑 N이 2일때 좀 다름

    # 0 5 5 0 이면 봉우리 있는거다!!!!!

    # 예외가 너무 많으면 if말고 그냥 while쓰자.
    '''
    문제의 '맨 앞쪽지형'이라는게 +3 인덱스까지 같은높이면 +3까지 그 조건이 계속 유지되는건가?
    
    마지막 인덱스 제외하고 지금 높이보다 낮아지면 봉우리 하나. cnt += 1
    현재 높이가 이전 높이보다 높으면 is봉우리 실행
        처음 실행한 인덱스 기억한다.
        
        is 봉우리 실행한 인덱스에서 진행했을때
        높이가 같으면 pass
            같으면 pass로 계속 넘긴다...
            
        높이가 더 낮아졌을때, break cnt += 1
            만약 pass로 넘긴 인덱스 들이있다면, 그만큼 더해서 그 다음 인덱스 진행
            ex) i = 4에서 시작해서 i = 7까지 높이 같고, 
                i = 8에서 내려감. 4,5,6,7이 한 봉우리.
                다음 인덱스는 i = 8에서 시작
        
        높이가 더 크면 break.
            현재 높이가 이전 높이보다 크므로 is봉우리 실행
            그냥 인덱스 +1
    
    i = 1일때는 무조건 함수 실행.
    i = N-1일때는 
        끝 인덱스가 함수 실행중인 인덱스에 포함되는가?
            = N-2인덱스와 높이가 같은가
        아니면 전 인덱스보다 높아졌는가
            이건 봉우리, cnt+=1
        전 인덱스보다 낮아졌는가
            그냥 pass
    '''
    i = 0
    cnt = 0

    while i <= N-1:
        if i == N-1 and arr[i] > arr[i-1]:    # 마지막 i가 봉우리검사 안거치고 시행됬고, 높이가 이전 높이보다 높다면, 봉우리임
            cnt += 1
            break

        if arr[i] > arr[i-1] or i == 0:       # 이번 높이가 이전 높이보다 크다면 or 첫 번째 지형이라면

            for j in range(i+1, N):     # 다음인덱스부터 체크

                if j == N-1:    # 끝 인덱스라면 for j 시작한 지금부터 전부 한 봉우리
                    cnt += 1
                    break

                if arr[i] > arr[j]:     # 봉우리가 한칸일때
                    cnt += 1
                    break

                # 높이 같으면 계속 넘어감, 높이 달라질 때 체크
                if arr[j] > arr[j+1]:    # 다음 높이보다 클 경우 봉우리임.
                    cnt += 1
                    i = j+1     # 다음 시행 j+1 인덱스부터 시작
                    break

                elif arr[j] < arr[j+1]:     # 다음 높이보다 작으면 봉우리 아니었던 것
                    i = j+1     # 다음 시행 j+1 인덱스부터 시작
                    break

                elif arr[j] == arr[j+1]:
                    continue

                break
        i += 1

    print(f'#{test_case} {cnt}')

'''
10개 중 6개만 맞는다...

'''