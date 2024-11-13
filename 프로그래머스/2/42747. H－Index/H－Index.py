def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    print(citations)
    for i in range(len(citations)):
        if i >= citations[i]:
            answer = i
            break
        else:
            answer = len(citations)
    return answer