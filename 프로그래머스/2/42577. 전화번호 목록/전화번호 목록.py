def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        for j in range(len(phone_book[i])):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                answer = False
    return answer