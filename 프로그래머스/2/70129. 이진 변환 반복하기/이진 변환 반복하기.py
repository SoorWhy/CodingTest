def solution(s):
    answer = []
    zero = 0
    times = 0
    while s != "1":
        zero += s.count("0")
        s = s.replace("0", "")
        s = bin(int(len(s)))[2:]
        times += 1
    answer = [times, zero]
    return answer