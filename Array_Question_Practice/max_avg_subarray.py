"""
Given an integer array and integer k, find the contiguous subarray of length k with the maximum average value.

nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75  (subarray [12,-5,-6,50])

nums = [5], k = 1
# Output: 5.0

"""

def max_avg(nums: int, k: int):

    total = sum(nums[0:k]) # Current sum till the k size window
    best_total = total

    for i in range(k, len(nums)):

        #print(i,k)

        left_ele = nums[i - k] # Getting the left element to be subtracted from total
        #print("Left Ele: ", left_ele)

        right_ele = nums[i] # Getting the right element to be Added in total
        #print("Right Ele: ", right_ele)

        total = (total - left_ele + right_ele) / k 

        window = nums[i - k : i]

        print(f"Window: {window} = {total}")

        if total > best_total:
            best_total = total
    
    return f" Best Total: {float(best_total)}"


nums1 = [1,12,-5,-6,50,3]
k = 4

nums2 = [5]
k2 = 1

print(max_avg(nums1, k))

