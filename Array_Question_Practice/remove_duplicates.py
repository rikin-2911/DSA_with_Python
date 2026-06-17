"""
Remove duplicates in the Sorted array

Given a sorted array, remove duplicates in-place so each element appears only once. Return the count of unique elements. Do not allocate extra space for another array.

nums = [1, 1, 2]
# Output: 2, nums = [1, 2, _]

nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

"""

def remove_duplicates(nums):
    if not nums:
        return 0
    
    left_pointer = 0

    for right_pointer in range(1, len(nums)):
        if nums[right_pointer] != nums[left_pointer]:
            left_pointer += 1
            nums[left_pointer] = nums[right_pointer]

    return left_pointer + 1


nums1 = [1,1,4]
nums2 = [0,0,1,1,1,2,2,3,3,4]

n = remove_duplicates(nums2)
print(n)
print(nums2[:n])


