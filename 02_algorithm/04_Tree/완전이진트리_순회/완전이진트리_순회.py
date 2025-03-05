# 완전이진트리에서의 순회
def pre_order(v):
    if v <= last:                   # 마지막 정점 이내
        print(tree(v))                    # 할 일
        pre_order(2*v)              # 왼쪽
        pre_order(2*v+1)            # 오른쪽
        # 부모가 v일때 자식이니까 2*v, 2*v+1이다.


# 보통 후위순회를 많이 쓴다


tree = [0, 1, 2, 3, 4, 5, 6, 7]
last = 7
pre_order(1)
