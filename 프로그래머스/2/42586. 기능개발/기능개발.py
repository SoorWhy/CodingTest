from collections import deque

def solution(progresses, speeds):
    answer = []
    count = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count > 0:
            answer.append(count)
            count = 0
            
    return answer