def solution(clothes):
    answer = 0
    count = 1
    clothes_dic = dict(clothes)
    clothes_set = set(clothes_dic.values())
    name_list = []
    for i in clothes_dic.values():
        name_list.append(i)
    for i in clothes_set:
        count *= (name_list.count(i) + 1)
    answer += (count-1)
    return answer