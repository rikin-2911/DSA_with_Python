"""
Given an array of integers nums and a target integer, return the indices of the two numbers that add up to the target. You may not use the same element twice.

First solve it in O(n²) with a nested loop, then optimize to O(n) using a dictionary.

nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

nums = [3, 2, 4], target = 6
# Output: [1, 2]
"""


# O(n^2)
def brute_force_2_sum(nums, target):

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j], nums[i], nums[j]


# Optimize method using Hash map or Hashing using Dictionary -> O(n^2) ---> O(n)
def optimize_two_sum(nums, target):

    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], i]
        
        num_dict[num] = i

    return []

nums = [2, 7, 11, 15, 82, 20]
target = 102
print(brute_force_2_sum(nums, target))
print(optimize_two_sum(nums, target))