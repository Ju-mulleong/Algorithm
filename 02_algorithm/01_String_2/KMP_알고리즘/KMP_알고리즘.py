def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)
    # preprocessing
    j = 0   # 일치한 개수 == 비교할




