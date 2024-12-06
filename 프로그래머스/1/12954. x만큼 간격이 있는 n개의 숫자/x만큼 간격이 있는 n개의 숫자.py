def solution(x, n):
    answer = []
    up = x
    for i in range(n):
        answer.append(x)
        x += up
    return answer