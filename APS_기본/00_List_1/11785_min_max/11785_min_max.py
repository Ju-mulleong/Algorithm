import sys
sys.stdin = open("input.txt", "r")

T = int(input())    # test case의 수 T
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

    N = int(input())    # 첫 줄에 양수의 개수 N
    num = list(map(int, input().split()))   # N개의 양수를 요소로 가지는 list num

    min_num = num[0]
    max_num = num[0]
    for n in num :
        if n > max_num :
            max_num = n

        if n < min_num :
            min_num = n

    difference = max_num - min_num

    print(f'#{test_case} {difference}')


