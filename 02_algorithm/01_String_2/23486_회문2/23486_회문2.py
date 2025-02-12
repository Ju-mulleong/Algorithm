import sys
sys.stdin = open('input.txt', 'r')

T = 10


def find_palindrome(N, arr):
    # 행 우선 탐색
    len_p = 0
    max_len = 0
    for arr_row in arr:
        for j in range(N):
            for length in range(N-j, max_len, -1):
                if arr_row[j:j + length] == arr_row[j:j + length][::-1]:  # 올바른 슬라이싱 사용
                    max_len = length
                    break

    return max_len


for test_case in range(1, 1+T):

    tc = int(input())   # 테스트 케이스의 번호 tc
    N = 100     # N*N 사이즈의 글자판

    arr = [list(input()) for _ in range(100)]
    # print(arr)
    # print(arr)

    # 가로 세로를 모두 보아 가장 긴 회문 길이 출력

    # 행 우선 탐색, 열 우선 탐색 각각 실행하면될듯
    # 가장 긴 길이 출력하니까 탐색에서 각 시행마다
    # 최대 길이 찾고, 다음 열에서는 그 최대길이 미만은 검사 안한다.
    # 긴 길이부터 탐색
    # 오늘 배운거?

    '''
    일단 가장 길게 [0], [99] 탐색하고
    다음 [1], [98] 하는데 틀렸다?
        그러면 [1], [99] 검사
            그런데 [99]의 값을 기억하고 있으니까 
            검사 전에 [1], [2], ...이 [99]의 값과 다르면 skip
            이걸 반복하면 될듯?
            
    회문의 길이를 정해놓고 하나씩 내릴까 
        이건 진짜 너무 오래걸릴듯
    그냥 슬라이싱?
    '''

    max_row = find_palindrome(N, arr)
    # print(max_row)

    arr = [list(x) for x in (zip(*arr))]     # 열에서도 회문 찾기 위해 전치행렬로 바꿈
    # print(arr)

    max_column = find_palindrome(N, arr)
    # print(max_column)

    if max_row >= max_column:
        print(f'#{tc} {max_row}')

    elif max_row < max_column:
        print(f'#{tc} {max_column}')

    elif max_row == max_column and max_row == 0:
        print(f'#{tc} {0}')


















'''
실패
   
# if N - j <= len_palindrome:  # 이번 시행이 회문이라도 앞에서 구해놓은 회문의 길이보다 짧으면 시행 안하고 break
#     break
# 
# if p_value != ' ' and p_value != arr[i][j]:     # 첫 시행이 아니고 시작값이 전에 기억했던 끝인덱스의 값인 p_value와 다를 경우
#     break
# 
# if arr[i][j] != arr[i][-1 - j]:     # 회문 아니면...
#     p_value = arr[i][-1 - j]
#     print(f'p_value:{p_value}')
#     break

'''


