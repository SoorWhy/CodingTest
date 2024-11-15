def solution(n):
    answer = []
    def hanoi(floor, src, dest):
        result = []
        mid = 6 - src - dest
        if floor>1:
            result += hanoi(floor-1, src, mid)
            result += [[src, dest]]
            result += hanoi(floor-1, mid, dest)
            return result
        else:
            return [[src, dest]]
    answer = hanoi(n, 1, 3)
    
    return answer