def solution(genres, plays):
    answer = []
    # 중첩 딕셔너리 생성
    genres_dic = {}
    for i in set(genres):
        genres_dic[i] = {}
    for i in range(len(genres)):
        genres_dic[genres[i]][i] = plays[i]
    
    # 장르별 우선순위 구하기
    max_dic = {}
    for i in genres_dic.keys():
        max_dic[i] = sum(list(genres_dic[i].values()))
    sum_dic = dict(sorted(max_dic.items(), key=lambda x: x[1], reverse=True)).keys()
    
    # 재생 수별 우선순위 구하기
    for i in sum_dic:
        sorted_dic = dict(sorted(genres_dic[i].items(), key=lambda x: x[1], reverse=True)).keys()
        genres_len = len(sorted_dic)
        if genres_len >= 2:
            answer.append(list(sorted_dic)[0])
            answer.append(list(sorted_dic)[1])
        else:
            answer.append(list(sorted_dic)[0])
        
    return answer