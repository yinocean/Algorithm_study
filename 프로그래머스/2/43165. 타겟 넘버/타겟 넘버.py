def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        add_ = dfs(index + 1, current_sum + numbers[index])
        sub_ = dfs(index + 1, current_sum - numbers[index])
        
        return add_ + sub_
    
    return dfs(0, 0)