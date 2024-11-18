def solution(brown, yellow):
    answer = []
    i = 1
    while 1:
        if (yellow/i + 2) * 2 + i*2 == brown:
            answer = [(yellow/i+2), i+2]
            break
        else:
            i += 1
    return answer