# 최대힙 (99개의 값 저장 가능한)

# 삽입
def enq(n):
    global last     # 마지막 정점
    last += 1
    heap[last] = n  # 마지막 정점에 n 저장

    c = last        # 부모의 키값과 비교하기 위해
    p = c // 2      # 부모 정점 번호 계산       # 완전이진트리라 p = c//2
    while p!=0 and heap[p] < heap[c]:   # 부모가 있고, 부모 키값 < 자식 키값 (최대힙 조건 위반)
        heap[p], heap[c] = heap[c], heap[p]     # 부모 자식 키값 교환
        c = p   # 현재 부모를 자식으로
        p = c // 2  # 부모의 부모를 다시 검사

    '''
    c, p는 노드번호 heap[]은 키값
    '''

# 삭제
def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    # 지금까지가 사실상 루트의 값을 따로 저장한 뒤, 마지막 노드를 옮겨서 루트에 덮어 씌운것과 같다.

    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p*2                 # 왼쪽 자식     # 완전이진트리에서 자식이 하나만 있는다면, 무조건 왼쪽자식이다.
    while c <= last:        # 자식이 하나라도 있으면  # 자식이 없다 == 계산한 자식의 노드번호가 last를 넘어간다.
        if c + 1 <= last and heap[c] < heap[c+1]:   # 오른쪽 자식도 있고, 오른 쪽 자식이 더 크면
            c += 1          # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c           # 자식을 새로운 부모로
            c = p * 2       # 왼쪽 자식 번호를 계산
        else:
            break
    return tmp
    # 루트에서 받아놨던 값 return

heap = [0]*100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
print(heap)

# 노드 계속 꺼내기
while last:
    print(deq())
