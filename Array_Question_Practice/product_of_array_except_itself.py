"""
Given an integer array nums, return an array where each element at index i is the product of all elements in nums except nums[i]. You must solve it without using division.

nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]
"""

def product_except_itself(nums):
    
    n = len(nums)
    result = [1] * n

    # Prefix prod
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # suffix prod
    suffix = 1
    for i in range(n -1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result


nums = [1,2,3,4]
print(product_except_itself(nums))
    