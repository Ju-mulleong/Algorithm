'''
N개의 숫자로 구성된 숫자열 Ai (i =1~N)와 M개의 숫자로 구성된 숫자열 Bj(J = 1~M)가 있다.

Aj나 Bj를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
(위치를 변경한다는 뜻이지 숫자들의 순서를 변경하는건 아니다!!)
단, 더 긴 쪽의 양 끝을 벗어나서는 안된다.

'서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.'

N과 M은 3이상 20이하이다.
맨 위 첫 줄: 테스트 케이스의 개수 T
첫 번째 줄: N, M
두 번째 줄: Aj
세 번째 줄: Bj

'''

'''
1. 테스트 케이스의 개수 T 읽어서 tc에 할당
2. N,M 읽어서 더 큰 수 파악 
3. Aj, Bj 읽어서 각각 리스트에 저장
4. 곱으로 나올 수 있는 경우의 수의 개수
	큰 수 - (작은 수 -1) 
	ex) N = 5, M = 7 이면, 나올 수 있는 경우의 수의 개수는
	7 - (5-1) = 3개 이다.
		작은 수의 맨 마지막수가 점점 하나씩 증가해서 끝값까지 도달한다고 생각해보자.
5. 예를 들어서 위 예시대로 하면, attempts는 3이다.
	A[:] * B[:N] 	# B에서 [0]부터 [4]까지
	A[:] * B[1:N+1]	# B에서 [1]부터 [5]까지
	A[:] * B[2:N+2]	# B에서 [2]부터 [6]까지

	리스트 원소끼리 곱하려면 원소의 개수가 같아야 하므로, 더 긴 리스트에서 슬라이싱하여 새로운 리스트 만들기!
	리스트 컴프리헨션과 zip()사용
	zip()은 두 리스트의 동일한 인덱스에 있는 원소를 묶어줌.
	list1 = [1,2,3]
	list2 = [4,5,6]

	result = [a*b for a,b in zip(list1,list2)]

6. 이렇게 각 i마다 시행한 결과들을 나올때마다 그 전 값과 비교하여 최댓값만 살려서 출력

7. 각 tc별로 반복


'''
import sys

sys.stdin = open("input.txt", "r")

tc = int(input())  # 맨 위 첫 번째 줄에서 test case 수 받기

# print(list_A,list_B)


for tcn in range(tc):
    N, M = map(int, input().split())  # N,M 읽기

    list_A = list(map(int, input().split()))  # Aj 값 리스트에 저장
    list_B = list(map(int, input().split()))  # Bj 값 리스트에 저장

    # print(list_A)
    # print(list_B)
    attempts = 0

    if N > M:  # N, M 비교하여 시행회수 attempts 구하기기
        attempts = N - (M - 1)
    elif N < M:
        attempts = M - (N - 1)
    else:
        attempts = 1

    try_max = 0
    result = []

    for i in range(attempts):

        # list_A[:] * list_B[i:attempts+i]
        if N < M:
            result = [a * b for a, b in zip(list_A, list_B[i:len(list_A) + i])]
        elif N > M:
            result = [a * b for a, b in zip(list_A[i:len(list_B) + i], list_B)]
        else:
            result = [a * b for a, b in zip(list_A, list_B)]

        # print(result)
        # print(sum(result))
        if sum(result) > try_max:
            try_max = sum(result)
        # print(try_max)
    print(f'#{tcn + 1} {try_max}')

# 정리 :attempts는 시도횟수고, 얼마만큼의 길이를 slicing 해야하는 지는 순전히 더 짧은 길이의 list만큼이다!!!



