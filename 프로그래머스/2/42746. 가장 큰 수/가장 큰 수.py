def solution(numbers):
    answer = ''
    num_list = list(map(str, numbers))
    num_list = sorted(num_list, key=lambda x: x*3, reverse=True)
    
    answer = ''.join(num_list)
    if answer[0] == '0':
        answer = '0'
    return answer