from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    
    while q:
        curr, depth = q.popleft()
        if curr == target:
            return depth
        
        for word in words:
            diff = 0
            for i, j in zip(curr, word):
                if i != j:
                    diff += 1
            if diff == 1:
                q.append((word, depth+1))
        