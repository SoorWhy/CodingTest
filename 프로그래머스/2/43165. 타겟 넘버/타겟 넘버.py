def solution(numbers, target):
    answer = 0
    
    def dfs(numbers, target, current_num, idx):
        if idx == len(numbers):
            if current_num == target:
                return 1
            else:
                return 0
        
        return dfs(numbers, target, current_num+numbers[idx], idx+1) + dfs(numbers, target, current_num-numbers[idx], idx+1)
    
    answer = dfs(numbers, target, 0, 0)
    return answer