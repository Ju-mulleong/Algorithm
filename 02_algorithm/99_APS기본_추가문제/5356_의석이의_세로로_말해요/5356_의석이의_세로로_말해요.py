import sys
sys.stdin = open('input.txt', 'r')  # input.txt

T = int(input())


# 한 줄에 최대 15글자로 이루어진 텍스트가 다섯 줄 input으로 주어진다.
# 이 텍스트들 세로로 읽기
# 텍스트의 길이는 다 다르다. 만약 세로로 읽었을 때 빈 칸이 있다면 그 칸은 무시하고 다음 글자를 읽는다.
# 세로로 읽은 순서대로 공백없이 출력하기

'''
1. 전치행렬로 읽기
    zip()에서 iterable들의 크기가 다르면 제일 작은 크기에 맞춰지는걸로 알고있다.
    이렇게 하면 까다로울듯

2. 읽는건 평소처럼 행 우선순회로 input 받고, 제일 길이가 긴 줄의 길이에 맞춰서 읽는다.
    만약 최대 길이 기준으로 빈 칸이 있으면, 그 칸은 ''로 넣는다.
    for로 열 우선순회로 읽어서 빈 문자열에 += 한다. 여기서 읽던 중 ''이 나오면 문자열에 추가하지않고 다음 반복으로 넘어간다.
'''

# 한 줄에 공백없이 텍스트 주어진다.
# for 로 한 글자씩 list에 넣어야하나?

for test_case in range(1, 1+T):

    arr = [list(input()) for _ in range(5)]     # testcase마다 5줄씩 주어진다.
    # print(arr)

    '''
    list() 는 iterable한 객체를 리스트로 변환.
    [] 는 직접 감싸는 것.
    '''

    # 2차원 배열 arr의 원소에서 길이가 가장 긴 list를 찾고,
    # 그 길이보다 짧으면 그만큼 그 list에 -1 append하기.

    # arr의 원소들의 길이 중 최대 길이 구하기
    max_length = len(arr[0])
    for i in range(len(arr)):
        if len(arr[i]) > max_length:
            max_length = len(arr[i])

    # 다시 arr을 순회하여 최대길이로 모든 원소list들 길이 맞추기
    # 짧으면 그만큼 ' ' append하기.
    for lst in arr:
        if len(lst) < max_length:
            append_cnt = max_length - len(lst)

            for _ in range(append_cnt):
                lst.append('')

    # 완성된 arr을 열 우선순회로 문자열 만들기

    ans = ''
    for j in range(max_length):
        for i in range(len(arr)):
            if arr[i][j] == ' ':
                continue
            ans += arr[i][j]

    print(f'#{test_case} {ans}')

'''
백준의 10798 세로읽기와 같은 문제

'''

