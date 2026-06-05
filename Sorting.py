# Bubble Sort

def sortArray(nums):
    n = len(nums)

    for i in range(n):
        isSwap = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                #swap
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isSwap = True

        if not isSwap:
            break

    return nums
    
print(sortArray([1,3,6,5,3,2,235,45,567,456,345234,123,234,3453456]))