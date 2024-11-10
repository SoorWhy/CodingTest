def solution(s):
    answer = ''
    list = []
    for i in s.split(' '):
        list.append(int(i))
    min_num = min(list)
    max_num = max(list)
    answer = str(min_num) + ' ' + str(max_num)
    return answer