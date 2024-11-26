import math

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    a = s // n
    b = s % n
    print(a, b)
    answer = [a] * n
    
    for i in range(b):
        answer[i] += 1
        
    answer.sort()
    return answer