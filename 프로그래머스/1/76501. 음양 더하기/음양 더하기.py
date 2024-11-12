def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign == 1:
            answer += num
        elif sign == 0:
            answer -= num
    return answer