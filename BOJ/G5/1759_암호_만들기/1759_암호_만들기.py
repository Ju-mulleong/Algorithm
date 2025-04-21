import sys
sys.stdin = open('input.txt', 'r')

'''

'''


# dfs(모음의 개수, 자음의 개수)
def dfs(i, j, idx, password):
    global visited

    # 종료조건
    if len(password) == L:
        # 모음의 개수가 0개거나, 자음의 개수가 1개 이하면 출력 x
        if i == 0 or j <= 1:
            return
        print(password)
        return

    # 가지치기

    for ii in range(idx, C):
        # 이번 글자가 모음이라면,
        if password_lst[ii] in lst_c:
            if visited:
                continue
            visited[ii] = 1
            dfs(i+1, j, idx+1, password+f'{password_lst[ii]}')
            visited[ii] = 0

        # 이번 글자가 자음이라면
        else:
            if visited:
                continue
            visited[ii] = 1
            dfs(i, j+1, idx+1, password+f'{password_lst[ii]}')
            visited[ii] = 0

        # # dfs 나오면 인덱스만 증가
        # dfs(i, j, idx + 1, password)


check = ['a', 'e', 'i', 'o', 'u']

# L은 암호의 길이, C는 주어진 문자의 개수
L, C = map(int, input().split())
visited = [0]*C

password_lst = list(input().split())

password_lst.sort()    # 정렬 해준다.


lst_c = []  # 주어진 문자들에서 모음만 따로
lst_v = []  # 주어진 문자들에서 자음만 따로
for i in range(C):
    if password_lst[i] in check:
        lst_c.append(password_lst[i])
    else:
        lst_v.append(password_lst[i])

print(password_lst)
print(lst_c)
print(lst_v)

len_c = len(lst_c)
len_v = len(lst_v)

# # 모음 개수 정하기
# for i in range(1, len_c+1): # 모음의 개수 1개부터 ~ 전체
#     # 모음 개수가 암호 길이 넘어가면 안 된다.
#     if i > L:
#         break
#
#     # 자음 개수 정하기
#     j = L-i
#     # 자음 개수 2보다 작으면 안 된다. or 전체 주어진 자음개수 넘어가면 안된다.
#     if j < 2 or j > len_v:
#         break

dfs(0, 0, 0, '')
