def solution(n):
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1
        answer = f1 % 1234567
    return answer