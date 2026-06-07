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

# def sortArray(nums):
#     n = len(nums)

#     for i in range(n):
#         mn = nums[i]
#         ind = i
#         for j in range(i+1, n):
#             if nums[j] < mn:
#                 mn = nums[j]
#                 ind = j

#         temp = nums[i]
#         nums[i] = nums[ind]
#         nums[ind] = temp

#     return nums

# print(sortArray([3, 2, 8, 1, 7, 6, 4]))




# Merge Sort

# def merge(nums, l, mid, r):
#     a = []
#     b = []

#     for i in range(l, mid+1):
#         a.append(nums[i])
#     for i in range(mid+1, r+1):
#         b.append(nums[i])

#     i, j, k = 0, 0, l

#     while k <= r:
#         if j == len(b):
#             nums[k] = a[i]
#             i += 1
#             k += 1
#         elif i == len(a):
#             nums[k] = b[j]
#             j += 1
#             k += 1
#         elif a[i] < b[j]:
#             nums[k] = a[i]
#             i += 1
#             k += 1
#         else:
#             nums[k] = b[j]
#             j += 1
#             k += 1


# def mergeSort(nums, l, r):

#     # base case
#     if l >= r:
#         return
    
#     # recursive case
#     mid = (l + r) // 2
#     # l to mid
#     mergeSort(nums, l, mid)
#     mergeSort(nums, mid+1, r)

#     merge(nums, l, mid, r)

# def sortArray(nums):
#     mergeSort(nums, 0, len(nums)-1)
#     return nums

# print(sortArray([3, 2, 8, 1, 7, 6, 4]))




# Quick Sort

# def partition(nums, l, r):
#     key = nums[r]
#     start = l

#     for i in range(l, r+1):
#         if nums[i] >= key:
#             temp = nums[i]
#             nums[i] = nums[start]
#             nums[start] = temp
#             start += 1

#     return start-1

# def quickSort(nums, l, r):
#     # base case
#     if l >= r:
#         return
    
#     p = partition(nums, l, r)

#     quickSort(nums, l, p-1)
#     quickSort(nums, p+1, r)
    
# def sortArray(nums):
#     n = len(nums)
#     quickSort(nums, 0, n-1)

#     return nums

# print(sortArray ([3, 2, 8, 1, 7, 6, 4]))




# Counting Sort

# def sortArray(nums):
#     n = len(nums)
#     mx = max(nums)

#     freq = [0] * (mx+1)

#     for i in nums:
#         freq[i] += 1

#     nums = []

#     for i in range(0, mx+1):
#         while freq[i] > 0:
#             nums.append(i)
#             freq[i] -= 1

#     return nums 

# print(sortArray([3, 2, 8, 1, 7, 6, 4]))