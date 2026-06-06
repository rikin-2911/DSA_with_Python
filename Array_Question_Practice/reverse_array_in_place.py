"""
You are given an array of integers. Without using any built-in reverse function, reverse the array in-place. Your solution must use O(1) extra space.

What is the time and space complexity of your approach?

arr = [1,2,3,4,5]
ans = [5,4,3,2,1]
"""

def custom_reverse(nums):

    left  = 0
    right = len(nums) - 1

    while left < right: # Key Insight from the question...
        nums[left], nums[right] = nums[right], nums[left] 
        left = left + 1
        right = right - 1
    
    return nums

arr1 = [1,2,3,4,5]
arr2  = [5,6,7,8,9]
arr3 = [4,7,2,8,2]
arr4 = [1,2,3,4,5,6,7,8]
arr5 = [2,3,4,4,2]

print(arr1)
print("Ans 1: ",custom_reverse(arr1))
print(arr2)
print("Ans 2: ",custom_reverse(arr2))
print(arr3) 
print("Ans 3: ",custom_reverse(arr3))
print(arr4)
print("Ans 4: ", custom_reverse(arr4))
print(arr5)
print("Ans 5: ",custom_reverse(arr5))
