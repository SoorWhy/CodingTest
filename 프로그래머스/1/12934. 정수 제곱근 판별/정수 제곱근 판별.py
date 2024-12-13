import math

def solution(n):
    answer = 0
    x = math.sqrt(n)
    if len(str(x).split('.')[1]) >= 2:
        return -1
    else:
        answer = (x+1) * (x+1)
    return answer