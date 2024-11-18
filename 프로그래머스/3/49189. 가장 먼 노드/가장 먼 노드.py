# from collections import deque

def solution(n, edge):
    answer = 0
    graph = {}
    # 연결된 노드 리스트 딕셔너리 생성
    for i in range(1, n+1):
        graph[i] = []
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    # 방문 안한 노드 = -1
    visited = [-1] * (n+1)
    visited[1] = 0 # 시작 노드는 0
    # q = deque([1])
    q = [1]
    
    while q:
        # curr = q.popleft() # 오른쪽 삽입, 왼쪽 pop
        curr = q.pop(0)
        for i in graph[curr]:
            if visited[i] == -1:
                visited[i] = visited[curr] + 1
                q.append(i)
    
    answer = visited.count(max(visited))
    return answer