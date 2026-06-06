# Bubble Sort

# def sortArray(nums):
#     n = len(nums)

#     for i in range(n):
#         isSwap = False
#         for j in range(n-i-1):
#             if nums[j] > nums[j+1]:
#                 #swap
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
#                 isSwap = True

#         if not isSwap:
#             break

#     return nums
    
# print(sortArray([3, 2, 8, 1, 7, 6, 4]))




# Insertion Sort

# def sortArray(nums):
#     n = len(nums)

#     for i in range(1,n):
#         key = nums[i]
#         j = i-1
#         while j >= 0 and nums[j] > key:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = key
        
#     return nums

# print(sortArray([3, 2, 8, 1, 7, 6, 4]))




# Selection Sort

def sortArray(nums):
    n = len(nums)

    for i in range(n):
        mn = nums[i]
        ind = i
        for j in range(i+1, n):
            if nums[j] < mn:
                mn = nums[j]
                ind = j

        temp = nums[i]
        nums[i] = nums[ind]
        nums[ind] = temp

    return nums

print(sortArray([3, 2, 8, 1, 7, 6, 4]))
