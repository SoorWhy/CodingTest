def solution(n, m):
    answer = []
    max_num = []
    
    if n > m:
        n, m = m, n
        
    for i in range(1, n+1):
        if m % i == 0 and n % i == 0:
            max_num.append(i)

    answer = [max(max_num), n * m // max(max_num)]
    return answer