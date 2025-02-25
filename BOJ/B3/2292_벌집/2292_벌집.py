num = int(input())

'''
이차원 배열로 하면 될듯?
배열 안의 배열의 크기가 행에 따라 다르도록,
1, 1*2+2*2, 3*2+3*2, 5*2+4*2,...
 
그냥 범위마다 6개씩 증가
'''

def f(N):
    M = 2*N-1
    return M*2+(N+1)*2

i = 2
while True:
    if num == 1:
        print(1)
        break

    elif f(i) < num < f(i + 1):
        print(i)
        break