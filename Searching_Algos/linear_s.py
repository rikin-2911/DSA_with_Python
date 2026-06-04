import time
def linear_search(nums, target):

    for i in range(len(nums)):

        if nums[i] == target:
            return i

    return -1



nums = [45, 12, 78, 23, 56, 89, 34]
print(linear_search(nums, 23))

