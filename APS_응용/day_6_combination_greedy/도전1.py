lst = ['A', 'B', 'C', 'D', 'E']
n = len(lst)

# 2명 이상의 친구를 선정하여 함께 카페에 가려고 한다.

# try1
for target in range(1 << n):
    temp = []
    for j in range(n):
       if 0x1 & (target >> j):       # target의 j번째 비트가 1인지 확인, j만큼 오른쪽으로 비트를 밀어서 확인하는 방식
           # print(lst[j])
           temp.append(lst[j])

    if len(temp) == 2:
        print(temp)



# 1인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    # for i in range(n):
    #     if tar & 0x1:
    #         cnt += 1
    #     tar >>= 1
    # return cnt

    # 같은 코드
    for i in range(n):
        if (tar >> i) & 0x1:
            cnt += 1
    return cnt


# 모든 부분집합중 원소의 수가 2개 이상인 집합의 수
ans = 0

for target in range(1 << n):
    # 만약 원소의 개수가 2개 이상이면, answer += 1
    if get_count(target) >= 2:
        ans += 1

print(ans)