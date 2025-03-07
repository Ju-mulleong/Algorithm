# 10개의 수를 입력받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
# 각 수는 0 이상 10000 이하의 정수이다.
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''
1. 테스트 케이스 개수를 입력받고 그 다음부터 0~10000의 정수들이 주어지므로, 
하드코딩하지 말고 테스트 케이스 만큼만 실행하는 코드 필요

" 정수 10개를 입력받아서 리스트에 저장하는걸 tc번 만큼 반복. "

앞으로 많이 쓸것같은데 test case = tc라 하자


2. 한 줄씩 tc번 실행하는 코드 필요
    한 줄마다 정수들을 공백을 기준으로 구분하여 리스트에 저장하고, 
    각 요소들이 홀수이면 result += 하자

    2.1 리스트에 정수 저장을 tc번만큼 반복

    2.2 정수가 홀수인지 확인하여 리스트에 저장하는 코드를 
        리스트의 길이만큼 반복

3. #t 정답 형태로 출력       


'''


tc = int(input()) # 테스트 케이스 개수 입력받아서 저장
result = 0  # 결과 초기화

int_lists = [[] for _ in range(tc)] # 테스트 케이스 개수만큼 리스트 생성하여 또 다른 리스트에 저장

for i in range(tc) :
    int_lists[i] = list(map(int, input().split()))  # 입력받은 정수를 공백을 기준으로 구분하여 리스트에 저장

for i in range(tc) :
    result = 0  # 테스트케이스 마다 결과 초기화
    
    for j in range(len(int_lists[i])) :    # 리스트의 길이만큼 반복
        

        int_num = int_lists[i][j]
        
        if int_num%2 != 0:
            result += int_num   # 리스트에 저장한 정수가 홀수이면 result에 더해서 저장
        
    print(f'#{i+1} {result}')    # f-string으로 출력
    



