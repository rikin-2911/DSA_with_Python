def binary_search(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:

        middle = (left + right) // 2 # Floor Division (Not Float)

        if nums[middle] == target:
            return middle
        
        elif nums[middle] < target:
            left = middle + 1  # GO TO RIGHT HALF

        else:
            right = middle - 1 # GO TO LEFt HALF
    
    return -1

nums = [12, 23, 34, 56, 78, 89]
print(binary_search(nums, 89))