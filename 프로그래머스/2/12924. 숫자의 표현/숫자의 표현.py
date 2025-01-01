def solution(n):
    answer = 0
    i = 1
    j = 1
    sum = 0
    count = 0
    while j<=n:
        if sum == n:
            sum = 0
            j += 1
            i = j
            count += 1
        elif sum > n:
            sum = 0
            j += 1
            i = j
        sum += i
        i += 1
    answer = count
    return answer