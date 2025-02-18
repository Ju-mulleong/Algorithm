def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    if i == N:  #
        print(p)
        # if-else문 아래의 생략된 return None 진행
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 교환한다.

            print('들어감')
            f(i+1, N)   # i+1자리 결정
            print('나옴')
            p[i], p[j] = p[j], p[i]     # f(i+1, N)이 return되면 다시 교환
        print('for j 끝')

p = [0,1,2]
N = 3
f(0, N)

'''
j가 중요하다. i, i+1, i+2... N-1이므로
'자기자신'도 포함해서 교환, 즉, p[i]와 p[i]를 바꿀 때도 있다.

교환하고 다음자리가고, 교환하고 다음자리가고, 
    i == N이면 print하고 돌아간다
    돌아가면 복구하고 for j 반복

'''