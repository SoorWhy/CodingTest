from collections import deque

def solution(arr):
    answer = []
    arr = deque(arr)
    
    while arr:
        start = arr.popleft()
        if not answer or answer[-1] != start:
            answer.append(start)
        
    return answer