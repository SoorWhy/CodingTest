def solution(n):
    answer = 0
    n = sorted(str(n), reverse=True)
    answer = ''.join(n)
    return int(answer)