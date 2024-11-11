def solution(nums):
    answer = 0
    answer = len(nums)/2
    if len(set(nums)) < answer:
        answer = len(set(nums))
    return answer