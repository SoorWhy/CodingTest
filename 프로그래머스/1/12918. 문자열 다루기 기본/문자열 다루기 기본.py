def solution(s):
    answer = True
    if not s.isdigit() or not len(s)==4 and not len(s)==6:
        answer = False
    return answer