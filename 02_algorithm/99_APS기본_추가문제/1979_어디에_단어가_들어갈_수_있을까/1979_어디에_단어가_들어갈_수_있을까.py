import sys
import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
단어의 길이가 딱 맞아야함!
일단 찾는 범위가 전부 1인가(단어를 쓸 수 있는 흰 칸인가)
가로방향으로 시작-1, 끝+1의 인덱스가 배열 밖이거나, 검은색 인덱스여야함.
세로방향도 마찬가지.
이것도 전치행렬로 재활용 되나?

흰색 부분이 1, 검은색 부분이 0

'''

def solve(arr):
    global cnt

    # 단어 가로로 자리 검색
    for i in range(N):
        flag = 0
        for j in range(N):
            if arr[i][j] == 1:
                flag += 1
            elif arr[i][j] ==0:
                flag = 0
            if flag == K:
                flag = 0
                if 0 <= j - K <= N - 1 and arr[i][j - K] == 0:
                    # 단어 왼쪽 끝-1이 정상인덱스이고 0이라면
                    if j + 1 == N:  # 오른쪽+1칸이 비정상인덱스라면
                        cnt += 1
                        # print(i, j)
                        continue
                    elif arr[i][j + 1] == 0:  # 오른쪽도 정상인덱스이고 0이라면
                        cnt += 1
                        # print(i, j)
                        continue

                elif j - K < 0:  # 단어 왼쪽 끝-1이 비정상인덱스라면
                    if j + 1 == N:  # 오른쪽 끝 +1이 비정상인덱스라면
                        cnt += 1
                        # print(i, j)
                        continue

                    elif arr[i][j + 1] == 0:  # 오른쪽도 정상인덱스이고 0이라면
                        cnt += 1
                        # print(i, j)
                        continue




for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    # N*N 크기의 배열, 단어의 길이 K
    # lst = list([1] * K)
    # print(lst)

    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint.pprint(arr)
    # arr은 N*N 크기의 배열

    solve(arr)
    arr = [list(x) for x in zip(*arr)]     # arr전치행렬로 바꾸기
    # pprint.pprint(arr)

    solve(arr)

    print(f'#{test_case} {cnt}')

'''
flag쓸거면 제대로 쓰자..
여기서는 연속으로 1이 K번나와야 하므로 0이 나오면 flag초기화 시켰어야했다.

전치행렬 제대로 쓰기
zip써야하니까 map처럼 list로 다시 묶어줘야함.
근데 zip은 튜플로 반환하므로 이걸 리스트로 바꾸려면 언패킹한다음에 다시 list로 묶어줘야함.
그래서 리스트 컴프리헨션 쓴거


'''