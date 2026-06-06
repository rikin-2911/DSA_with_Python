"""
Delete First Occurrence

Given a list, write a function to delete the first occurrence of a given value. Do not use the built-in .remove() method. Handle the case where the value does not exist.

What happens to the indices of all elements after the deleted element?

arr = arr = [10, 20, 30, 40, 20]
delete(arr, 20)
# Expected: [10, 30, 40, 20]
"""

def delete(nums, target):

    if len(nums) == 0:
        return f"List is empty !"
    
    for i in range(0, len(nums)):
        if nums[i] == target:
            del nums[i]
            break

    return nums, f" Length of New array: {len(nums)}"

arr = [10, 20, 30, 10, 75, 83]
print(delete(arr, 10))
        
"""
Solved: Using Linear Search and find the first occurence and delete it and shifted the indices to the left of the array.
T.C = O(n)
S.C = O(1)
"""