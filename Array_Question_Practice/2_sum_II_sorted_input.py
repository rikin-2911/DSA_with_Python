"""
Given a 1-indexed sorted array, find two numbers that add up to a target. Return their indices. You must use O(1) extra space.

numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]

numbers = [2, 3, 4], target = 6
# Output: [1, 3]
"""


def two_sum_sorted(nums, target):

    nums.sort()

    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer < right_pointer:

        result = nums[left_pointer] + nums[right_pointer]

        if result == target:
            return [left_pointer+1, right_pointer+1]
        
        elif result < target:

            left_pointer = left_pointer + 1

        else:

            right_pointer = right_pointer - 1

    return []


numbers = [2, 7, 11, 15]
target = 22
print(two_sum_sorted(numbers, target))
        
        
