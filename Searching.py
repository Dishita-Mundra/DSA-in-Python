# Linear Search

class Solution:
    def search(nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1
    
