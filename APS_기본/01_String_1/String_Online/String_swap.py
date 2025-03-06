txt = list(input())
N = len(txt)
for i in range(N//2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
print(txt)
