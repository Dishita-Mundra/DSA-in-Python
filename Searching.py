# Linear Search

class Solution:
    def search(nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1
    



# Binary Search

def search(nums, target):
        n = len(nums)

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1

        return -1