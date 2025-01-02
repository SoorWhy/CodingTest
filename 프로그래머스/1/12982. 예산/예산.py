def solution(d, budget):
    answer = 0
    d = sorted(d)
    count = 0
    for i in d:
        budget -= i
        count += 1
        if budget < 0:
            count -= 1
            break
    answer = count
    return answer