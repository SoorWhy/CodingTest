from collections import deque, defaultdict

def solution(info, edges):
    answer = 0
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
    
    sheep = 1
    wolf = 0
    visitable = set()
    q = deque([(0, sheep, wolf, visitable)])
    print(q)
    
    while q:
        curr, sheep, wolf, visitable = q.popleft()
        answer = max(answer, sheep)
        
        for i in graph[curr]:
            if i not in visitable:
                visitable.add(i)
        
        for i in visitable:
            if info[i] == 0:
                q.append((i, sheep+1, wolf, visitable - {i}))
            elif info[i] == 1 and sheep>wolf+1:
                q.append((i, sheep, wolf+1, visitable - {i}))
                
    return answer