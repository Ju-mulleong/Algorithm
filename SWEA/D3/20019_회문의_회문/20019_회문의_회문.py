import sys
sys.stdin = open('input.txt', 'r')


def is_pal_pal(s, n):
    # 일단 회문인지 확인
    # N//2만큼 검사
    for i in range(n//2):
        if s[i] != s[-1-i]:
            # 회문이 아니라면 "NO" return
            return "NO"

    else:
        # 회문이라면
        s1 = s[:(N-1)//2:]    # 회문회문 첫 째 조건 위한 슬라이싱
        # print(s1)
        for j in range(len(s1)//2):
            if s1[j] != s1[-1-j]:   # 회문회문 아니라면 return
                return "NO"

        else:
            # 회문회문 첫째 조건 통과했다면  #어차피 회문이니까 역순으로 슬라이싱해도됨
            s2 = s[-1:-(N-1)//2 - 1:-1]
            # print(s2)
            for k in range(len(s2)//2):
                if s2[k] != s2[-1-k]:
                    return "NO"

            else:
                # 회문회문 조건 다 통과하면 return "YES"
                return "YES"


T = int(input())

'''
회문의 회문
길이가 홀수 N인 문자열 S
일단 우리가 아는 회문 조건 만족 후,
    S의 처음 (N-1)/2 글자가 회문
    S의 마지막 (N-1)/2 글자가 회문
    
    N이 5면 처음/마지막 2글자
    N이 7이면 처음/마지막 3글자
    N이 9이면 처음/마지막 4글자..
'''

for test_case in range(1, 1+T):
    S = input()
    N = len(S)
    ans = is_pal_pal(S, N)
    print(f'#{test_case} {ans}')