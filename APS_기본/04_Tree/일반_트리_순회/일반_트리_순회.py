'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(v):
    if v:
        print(v, end=' ')
        preorder(tree[v][0])
        preorder(tree[v][1])
        

V = int(input())        # 정점 수
E = V-1                 # 간선 수
temp = list(map(int, input().split()))
tree = [[0]*3 for _ in range(V+1)]   # 인접리스트 14 * 3

for i in range(E):
    p, c = temp[i*2], temp[i*2+1]
    if tree[p][0] == 0:  # 왼쪽 자식이 없으면
        tree[p][0] = c
    else:               # 왼쪽 자식이 있으면
        tree[p][1] = c
    tree[c][2] = p      # 부모 저장

# for i in tree:
#     print(i)

# root 찾기
lst = []    # 조상 저장하기
c = V
while tree[c][2]:
    c = tree[c][2]
    lst.append(c)
root = c
print(lst, root)

