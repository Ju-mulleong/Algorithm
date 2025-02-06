def counting_sort(data, temp, K):
    # 1. 카운팅
    cnts = [0] * (K + 1)    # index는 0부터니까 +1 해서 만들어야됨
    for i in range(N):
        cnts[data[i]] += 1
    print(cnts)
    # 2. 누적
    for i in range(1, K + 1):   # K = 4 / 1, 2, 3, 4
        cnts[i] += cnts[i-1]    # cnts[i] = cnts[i] + cnts[i-1]
    print(cnts)
    # 3. 배치
    for i in range(N-1, -1, -1):
        cnts[data[i]] -= 1     # 결과 배열에 들어갈 index
        print(cnts)
        temp[cnts[data[i]]] = data[i]



data = [0, 4, 1, 3, 1, 2, 4, 1] # 원본
N = len(data)
K = max(data)   # 최댓값
temp = [0] * N   # 결과
counting_sort(data, temp, K)
print(temp)



# counting_solt는 비파괴. 원본 바꾸려면 복사해줘야됨.

# 도전 과제: 내림차순은 어떻게 해야 할까요?