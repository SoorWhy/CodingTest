def solution(s):
    answer = []
    s_list = s.split(' ')
    for i in s_list:
        word = ''
        for j in range(len(i)):
            if j % 2 == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        answer.append(word)
    answer = ' '.join(answer)
    return answer