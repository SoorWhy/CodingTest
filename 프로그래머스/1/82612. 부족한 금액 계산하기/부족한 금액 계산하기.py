def solution(price, money, count):
    answer = -1
    total = 0
    tmp = price
    for i in range(1, count+1):
        price *= i
        total += price
        price = tmp
    answer = total - money
    if answer <= 0:
        answer = 0
    return answer