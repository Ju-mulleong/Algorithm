import sys
sys.stdin = open('input.txt', 'r')

T = 10  # 테스트 케이스의 개수 T


def find_palindrome(arr, N):
    global cnt

    # 행 우선 탐색 모양
    for arr_row in arr:
        for j in range(8 - N + 1):
            now_arr = arr_row[j: j + N]  # 회문 검사할 list 슬라이싱하기
            for c in range(N // 2):
                if now_arr[c] != now_arr[-1 - c]:  # 만약 회문이 아니라면 빠져나가서 다음 슬라이싱한 list 검사
                    break
                if c == (N // 2) - 1:
                    cnt += 1  # break 안당하고 마지막 인덱스까지 for문 마치면(회문이면) cnt += 1


for test_case in range(1, 1+T):
    N = int(input())    # N은 찾아야하는 회문의 길이
    cnt = 0
    arr = [list(input()) for _ in range(8)]
    # print(arr)

    # 가로 또는 세로로 이어진 회문만 구하면되므로, 행 우선 탐색 1번, 열 우선 탐색 1번 돌리면 되나?
    # 회문의 길이 N이 매 시행마다 주어진다.
    # 행 우선 탐색 기준으로, 한 행에서 길이를 N으로 슬라이싱 (8-N + 1)번 하면 된다.
    # 슬라이싱 한 뒤, N // 2 만큼 "[i] == [-1 - i]" 비교 반복 하면됨.

    # 행 우선 탐색
    find_palindrome(arr, N)
    # print(cnt)

    # arr을 전치행렬로 바꾸면 열 우선 탐색 할 때 위의 코드 재사용할 수 있지 않나?
    arr = list(zip(*arr))
    # print(arr)

    find_palindrome(arr, N)
    # print(cnt)

    print(f'#{test_case} {cnt}')
