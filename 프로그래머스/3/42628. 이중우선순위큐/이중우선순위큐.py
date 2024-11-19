def solution(operations):
    answer = []
    q = []
    for i in operations:
        if 'I' in i:
            q.append(int(i.split(' ')[-1]))
        if 'D -1' in i and q:
            q.pop(q.index(min(q)))
        if 'D 1' in i and q:
            q.pop(q.index(max(q)))
    if not q:
        answer = [0, 0]
    else:
        answer = [max(q), min(q)]
    return answer