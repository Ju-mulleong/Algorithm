di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

i = 2
j = 3
for dir in range(4):
    ni = i +di[dir]
    nj = j +dj[dir]
    print(ni, nj)

