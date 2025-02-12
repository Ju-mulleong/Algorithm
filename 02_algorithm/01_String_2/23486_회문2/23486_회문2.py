import sys
sys.stdin = open('input.txt', 'r')

T = 10

def find_p(arr):
    len_p = 0   # 회문의 최대 길이

    # 길이 1짜리 회문이 최대일 경우도 생각해야함
    if arr == [[arr[0][0] for _ in range(100)] for _ in range(100)]:
        # 배열이 배열의 첫 원소로만 이루어진 배열과 같을 경우
        return 1

    for i in range(100):
        d = 0
        flag = 1
        len_temp = 100
        while len_temp >= 3:
            if flag == 1:
                for k in range(d+1):
                    for j in range(len_temp // 2):  # 보기처럼 N = 8이면 첫 시행에서 j = 0, 1, ... 3
                        # print(j+d, (len_temp - 1 - j) + d )
                        if arr[i][j + k] != arr[i][(len_temp - 1 - j) + k]:
                            break


                    else:   # break 없이 j 문 다 마치면(회문이면)
                        len_p = len_temp
                        # print(len_p)
                        flag = 0    # 위의 while도 실행 안 하도록
                        break

                # 회문이 아니어서 for j 빠져 나왔을때
                d += 1
                len_temp -= 1

                # 이전 반복에서 구한 회문의 길이와 다음 시행에서 검사할 회문의 길이가 같아지면,
                # 만약 다음 시행에서 회문이더라도 회문의 최대길이는 안 변하므로 다음 행으로 넘어가기
                if len_temp == len_p:
                    flag = 0
                    break
            else:
                break

    return len_p


for test_case in range(1, 1+T):
    tc = int(input())

    arr = [list(input()) for _ in range(100)]


    # 100*100의 배열 주어짐

    # 어렵게 생각하지말고 N길이 회문, N-1길이 회문... 찾기

    max_row = find_p(arr)

    max_column = find_p([list(x) for x in zip(*arr)])   # 전치행렬로 만들어서 같은 함수에 넣기

    print(f'#{test_case} {max(max_row, max_column)}')







'''
len = 7
[0] == [6]
[1] == [5]...

d + 1

[0 + 1] == [6 + 1]
[1 + 1] == [5 + 1]

'''



