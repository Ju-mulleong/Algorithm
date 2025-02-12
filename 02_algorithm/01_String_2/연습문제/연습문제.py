t = 'TTTTTATTAATA'
p = 'TTA'

N = len(t)  # 12
M = len(p)  # 3

# 고지식한 방법
def search(p, t):
    for i in range(N-M+1):  # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):  # p에서 비교할 위치 인덱스
            if t[i+j] != p[j]:
                break
        else:       # for-else문!!!!!!!!!    # break에 걸리지 않고 for문이 끝난 경우 else를 실행
            return i        # 패턴이 처음 나타난 인덱스 리턴

        return -1   # 패턴이 텍스트 내에 없을 경우


print(search(p, t))
