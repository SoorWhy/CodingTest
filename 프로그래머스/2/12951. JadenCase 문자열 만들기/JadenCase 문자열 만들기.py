def solution(s):
    answer = ''
    s = s.lower()
    s = s[0].upper() + s[1:]
    for i in range(len(s)-1):
        if s[i] == ' ':
            s = s[:i+1] + s[i+1].upper() + s[i+2:]
    answer = s
    
    return answer