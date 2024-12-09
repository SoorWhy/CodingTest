def solution(s):
    answer = True
    y_count = 0
    p_count = 0
    for i in s:
        if i == 'y' or i == 'Y':
            y_count += 1
        elif i == 'p' or i == 'P':
            p_count += 1
    
    if y_count == p_count:
        answer = True
    else:
        answer = False

    return answer